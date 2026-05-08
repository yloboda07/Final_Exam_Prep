class LabelGenerator:
    def __init__(self,prefix,n=1):
        self.prefix = prefix
        self.n = n
    def next_label(self):
        self.n+=1
        return f"{self.prefix}{self.n-1}"

#Checking 
figures = LabelGenerator("Figure ")
print(figures.next_label())
print(figures.next_label())
print(figures.next_label())



### OR

# class LabelGenerator: 
#     def __init__(self, prefix, start=1): 
#         self._prefix = prefix 
#         self._count = start 
#     def next_label(self): 
#         label = f"{self._prefix}{self._count}" 
#         self._count += 1 
#         return label

# # Checking
# figures = LabelGenerator("Figure ")
# print(figures.next_label())
# print(figures.next_label())
# print(figures.next_label())
