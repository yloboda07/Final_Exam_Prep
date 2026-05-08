class Domino:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __str__(self):
        return f"Domino ({self.left}, {self.right})"
    def get_left_dots(self):
        return self.left
    def get_right_dots(self):
        return self.right
    def will_match(self, n):
        return self.left == n or self.right == n
d = Domino(1,4)
print(d)
print(d.get_left_dots())
print(d.get_right_dots())
print(d.will_match(1))
print(d.will_match(2))

