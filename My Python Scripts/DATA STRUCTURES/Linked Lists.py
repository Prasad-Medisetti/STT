#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:59:31 2020

@author: prasadm

DATA STRUCTURES - LINKED LIST 
"""

class Node:
	def __init__(self, value=None):
		self.value = value
		self.next = None
		
	def isempty(self):
		'''Checks whether the list is empty or not'''
		return (self.value==None)

	def append(self,v):
		'''Appends a node with value v to the linked list'''
		if self.isempty():
			self.value = v
		elif self.next==None:
			nn = Node(v)
			self.next = nn
		else:
			(self.next).append(v)
	
	def insertb(self,v):
		'''inserts a node with value v to the linked list at the beginning'''
		if self.isempty():
			self.value = v
		else:
			nn = Node(v)
			(self.value,nn.value) = (nn.value,self.value)
			(self.next,nn.next) = (nn,self.next)
	
	def reverse_new(self):
		'''Revereses a list by creating new list'''
		if self.isempty():
			print('List is Empty...')
			return
		elif self.next==None:
			return 
		else:
			nn = Node(self.value)
			temp = self
			while(temp.next!=None):
				nn.insertb(temp.next.value)
				temp.next = temp.next.next
			(self.value,nn.value) = (nn.value,self.value)
			(self.next,nn.next) = (nn.next,self.next)
			
	
	def deletei(self,v):
		'''Deletes a node with value v from the linked list'''
		if self.isempty():
			print('List is Empty...')
			return
		elif self.value==v:
			if self.next==None:
				self.value = None
				return
			else:
				self.value = self.next.value
				self.next = self.next.next
				return
		else:
			temp = self
			while temp.next!=None:
				if temp.next.value==v:
					temp = temp.next
					return
				else:
					temp = temp.next
			else:
				print('No %d in List'%v)
	
	def deleter(self):
		'''Deletes last node from the linked list'''
		if self.isempty():
			print('List is Empty...')
		elif self.next==None:
			if self.value!=None:
				print (self.value,'is deleted...')
				self.value = None
			return
		elif (self.next).next==None:
			print((self.next).value,'is deleted...')
			self.next = None
			return
		else:
			(self.next).deleter()
	
	def show(self):
		'''Displays the linked list'''
		if self.isempty():
			print('List is Empty...')
		elif self.next==None:
			print(self.value,end=' ')
			return
		else:
			print(self.value,end=' ')
			(self.next).show()
			
	@classmethod
	def create_list(cls,l):
		'''Creates linked list with l'''
		n = Node()
		for i in l:
			n.append(i)
		return n
	
	@classmethod
	def concat(cls,l1,l2):
		'''Appends l2 at the ending l1'''
		temp = l1
		while temp.next!=None:
			temp = temp.next
		temp.next = l2
	
	@classmethod
	def reverse(cls,l):
		'''returns a linked list of reverse of linked list l'''
		prev_node = None
		current_node = l
		
		while current_node is not None:
			n = current_node.next
			current_node.next = prev_node
			prev_node = current_node
			current_node = n
		return prev_node
		
	def count(self):
		'''returns count of elements in the linked list using iteration'''
		cnt = 0
		temp = self
		while(temp!=None):
			cnt += 1
			temp = temp.next
		return cnt
	
	def countr(self):
		'''returns count of elements in the linked list using recursion'''
		temp = self
		if temp.next==None:
			return 1
		else:
			return 1+(temp.next).countr()
		
	def swap(self):
		'''swaps two nodes in the linked list'''
		if self.next==None:
			return
		else:
			(self.value, self.next.value) = (self.next.value, self.value)
			self.next.swap()
			
	def rotateleft(self, n = 1):
		'''circular rotation of linked list to left'''
		for i in range(1,n+1):
			self.swap()
			
	def rotateright(self):
		'''circular rotation of linked list to right'''
		t1 = self
		
		while t1.next.next!=None:
			t1 = t1.next
		t2 = t1.next
		
		t1.next = None
		self.insertb(t2.value)
	
	def sort(self):
		'''sorts linked list'''
		t1 = self
		t2 = self.next
		while t1!=None:
			t2 = t1.next
			while t2!=None:
				if t1.value>t2.value:
					t1.value, t2.value = t2.value, t1.value
				t2 = t2.next
			t1 = t1.next
						
	def min(self):
		'''returns minimum value present in linked list'''
		temp = self
		mn = temp.value
		while temp.value:
			if temp.value<mn:
				mn = temp.value
			temp = temp.next
			if temp==None:
				break
		return mn
	
	def max(self):
		'''returns maximumm value present in linked list'''
		temp = self
		mx = temp.value
		while temp.value:
			if temp.value>mx:
				mx = temp.value
			temp = temp.next
			if temp==None:
				break
		return mx
	
	@classmethod
	def addll(cls,l1,l2):
		t1 = l1
		t2 = l2
		while t1!=None and t2!=None:
			t1.value += t2.value
			
		return
								
if __name__=='__main__':
	pass

#	ll = Node()
#	ll.append(100)
#	ll.append(200)
#	ll.append(300)
#	ll.show()
#	print('\nReversed')
#	r = Node.reverse(ll)
#	r.show()
#	
	
#	temp = ll
#	while(temp.value):
#	    print(temp.value,end=' ')
#	    temp = temp.next
#	    if temp==None:
#	        break
	
	
	
	
# =========================================================================
