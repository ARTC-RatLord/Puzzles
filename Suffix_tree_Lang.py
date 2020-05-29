# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:39:11 2020

@author: 502598
"""

import os

os.chdir(r'C:\Users\502598\Documents\Python')
f=open("rosalind_lcsm (5).txt")
file=f.read()
file=file.replace('\n','')


class Node:
    """
    A node belongs to a suffix
     suffix_node
      the index of a node with a matching suffix, representing a suffix link.
      -1 indicates this node has no suffix link.
    """
    def __init__(self):
        self.suffix_node=-1

    
class Edge:
    """
    An edge in the suffix tree 
    first_char_index:
        index of start of string part represented by this edge
    last_char_index:
        index of end of string part represented by this edge
    """
    
    def __init__(self,first_char_index,last_char_index,source_node_index,dest_node_index):
        self.first_char_index=first_char_index
        self.last_char_index=last_char_index
        self.source_node_index=source_node_index
        self.dest_node_index=dest_node_index
    
    def __repr__(self):
        return 'Edge %d,%d,%d,%d'%(self.first_char_index,self.last_char_index,self.source_node_index,
                                   self.dest_node_index)
    
    @property
    def length(self):
        return self.last_char_index - self.first_char_index


    
class Suffix:
    """
    Represents a suffix from start to end.
    """
    
    def __init__(self,source_node_index,first_char_index,last_char_index):
        self.source_node_index=source_node_index 
        self.first_char_index=first_char_index
        self.last_char_index=last_char_index#active length
        
    
    @property
    def length(self):
        return self.last_char_index - self.first_char_index
    
    def explicit(self):
        """A suffix is explicit if it ends on a node. 
        is set greater than last_char_index to indicate this.

        """
        return self.last_char_index < self.first_char_index #if it is a leaf node, it ends with -1

    def implicit(self):
        return self.last_char_index > self.first_char_index # implicit in edge
    
class SuffixTree:
    """
    A SuffixTree is composed of nodes and edges
    
    Add suffix (which mark as self.active)
    can form a new edges (or some times with new nodes)
    
    """
    
    def __init__(self,stri):
        """
        read a string
        """
        self.stri=stri
        
        self.nodes=[Node()]
        self.edges={} 
        #edges is a dictionary, keys=[source_node_index,self.stri[i]]
        self.N=len(stri)-1
       
        
        self.active=Suffix(0,0,-1) #last_char_index=-1 #active point in other ref
         
        #active suffix is going to add into suffix tree each time

        for i in range(len(stri)):
            print(stri[i])
            self._add_prefix(i) #for comparison
        
        
            

    def __repr__(self):

        """ 
        Lists edges in the suffix tree
        """

        curr_index = self.N
        s = "\tStart \tEnd \tSuf \tFirst \tLast \tString\n"
        values = list(self.edges.values())
        #self.findlongest(values)
        values.sort(key=lambda x: x.source_node_index)
        for edge in values:
            if edge.source_node_index == -1:
                continue
            s += "\t%s \t%s \t%s \t%s \t%s \t"%(edge.source_node_index
                    ,edge.dest_node_index 
                    ,self.nodes[edge.dest_node_index].suffix_node 
                    ,edge.first_char_index
                    ,edge.last_char_index)

            top = min(curr_index, edge.last_char_index)
            
            s += self.stri[edge.first_char_index:top+1] + "\n"
            

        return s      
    
    def _add_prefix(self,last_char_index):
        
        last_parent_node=-1 #
        while True:
            parent_node=self.active.source_node_index
            #initial parent_node=0
            if self.active.explicit():
                if (self.active.source_node_index, self.stri[last_char_index])in self.edges:
                    #last_char_index=i
                   #initial prefix with node end is already in tree and point to root'0'
                    break
            else:#implicit
                e = self.edges[self.active.source_node_index, self.stri[self.active.first_char_index]]
                #initial source_node_index=0, first_char_index=0
                #this is for active point goes down
                if self.stri[e.first_char_index + self.active.length + 1] == self.stri[last_char_index]:
                   # prefix is already in tree
                   break   
                parent_node = self._split_edge(e, self.active)
               
            self.nodes.append(Node())
            e = Edge(last_char_index, self.N, parent_node, len(self.nodes) - 1)
            self._insert_edge(e)# generalize a new edge
        
        
            if last_parent_node > 0:
                self.nodes[last_parent_node].suffix_node = parent_node
                last_parent_node = parent_node
              
                
            if  self.active.source_node_index == 0:
                self.active.first_char_index += 1
               #active point walk down
    
            else:
                print(self.active.source_node_index)
                self.active.source_node_index = self.nodes[self.active.source_node_index].suffix_node


            self._canonize_suffix(self.active)
            #print(self.edges)
        
        if last_parent_node > 0:

            self.nodes[last_parent_node].suffix_node = parent_node

        self.active.last_char_index += 1
        self._canonize_suffix(self.active)
        
    def _split_edge(self, edge, suffix):
        
        self.nodes.append(Node())
        # generate new edge for the orighal edge
        e = Edge(edge.first_char_index, edge.first_char_index + suffix.length, suffix.source_node_index, len(self.nodes) - 1)
        self._remove_edge(edge)
        self._insert_edge(e)
        self.nodes[e.dest_node_index].suffix_node = suffix.source_node_index 
#        print(suffix.source_node_index)
#        print('*')
        # generate new edge for adding suffix
        ### need to add node for each edge
        #this edge have a suffix link match with (point to last active node)
        
        edge.first_char_index += suffix.length + 1
        edge.source_node_index = e.dest_node_index
        self._insert_edge(edge)

        return e.dest_node_index 
        
    def _insert_edge(self,edge):
        self.edges[(edge.source_node_index, self.stri[edge.first_char_index])] = edge

    def _remove_edge(self, edge):
        self.edges.pop((edge.source_node_index, self.stri[edge.first_char_index]))
        
    
    def _canonize_suffix(self, suffix):

        """This canonizes the suffix, walking along its suffix string until it 

        is explicit or there are no more matched nodes.

        """

        if not suffix.explicit():
            i=1
            while (suffix.source_node_index, self.stri[suffix.first_char_index]) not in self.edges:
                i=i+1
                self.active.source_node_index = self.nodes[self.active.source_node_index].suffix_node
                    
            e = self.edges[suffix.source_node_index, self.stri[suffix.first_char_index]]
            if e.length <= suffix.length:
                suffix.first_char_index  += e.length + i
                suffix.source_node_index = e.dest_node_index
                self._canonize_suffix(suffix)


#    def findlongest(self,values):
#        index={}
#        for i in values:
#            index[i.source_node_index]=[i.dest_node_index,i.length]
#        start=0
#        end=0
#        ln=0
#        ln_list=''
#        while True:
#            if
#             for k,v in index.items():
#                 if k==start:
#                    end=v[0]
#                    start=k
#                    ln+=v[1]
#                    ln_list+=self.stri[k:v[0]+1]
#                 end=start
#        print(ln_list)

        
String=SuffixTree(file)
print(String)
print(type(String))
#output = [consesus, Af,Cf,Gf,Tf]
#
#with open('consensusLang.txt', mode = 'w') as f:
#
#    for i in output:
#
#        f.write(i + '\n') 
    
with open('haha.txt',"w") as f:
    f.write(str(String))
    
    
