class Solution:
    def simplifyPath(self, path):
        stackDOF = []
        path = path.split('/')
        for element in path:
            if stackDOF and element == "..":
                stackDOF.pop()
            elif element not in [".", "..", ""]:
                stackDOF.append(element)
        return "/"+ "/".join(stackDOF)