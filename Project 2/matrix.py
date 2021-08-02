class matrix():
    def __init__(self,mat):
        self.r=len(mat)
        self.c=len(mat[0])
        self.matrix = mat

    def __add__(self,mat):
        if self.r==mat.r and self.c==mat.c:
            r=self.r
            c=self.c
            add_mat = []
            for i in range(r):
                add_mat.append([])
                for j in range(c):
                    temp=self.matrix[i][j]+mat.matrix[i][j]
                    add_mat[i].append(temp)
            return add_mat
        else:
            raise ValueError('Incompatible matrices')
    
    def __sub__(self,mat):
        if self.r==mat.r and self.c==mat.c:
            r=self.r
            c=self.c
            sub_mat = []
            for i in range(r):
                sub_mat.append([])
                for j in range(c):
                    temp=self.matrix[i][j]-mat.matrix[i][j]
                    sub_mat[i].append(temp)
            return sub_mat
        else:
            raise ValueError('Incompatible matrices')
    
    def __mul__(self,mat):
        if self.c==mat.r:
            r=self.r
            c=mat.c
            mul_mat = []
            for i in range(r):
                mul_mat.append([])
                for j in range(c):
                    temp = 0
                    for k in range(mat.r):
                        temp+=self.matrix[i][k]*mat.matrix[k][j]
                    mul_mat[i].append(temp)
            return mul_mat
        else:
            raise ValueError('Incompatible matrices')

    def det(self):
        if self.r == self.c :   
            det_mat = self.det_r(self.matrix)
            return det_mat   
        else :
            raise ValueError("Not a square matrix. Determinant can't be calculated")       

    def mat_minor(self,m,i,j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

    def det_r(self,m):
        if len(m) == 2:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]

        mat_det = 0
        for c in range(len(m)):
            mat_det += ((-1)**c)*m[0][c]*self.det_r(self.mat_minor(m,0,c))
        return mat_det
    
    def __pow__(self,n):
        if n == 1:
            return self.matrix
        elif self.r == self.c :  
            I = []
            for i in range(self.r):
                I.append([])
                for j in range(self.c):
                    if i==j :
                        I[i].append(1)
                    else:
                        I[i].append(0)
            exp_mat = matrix(I)
            for i in range(n):
                exp_mat.matrix = exp_mat.__mul__(self)
            return exp_mat.matrix
        else:
           raise ValueError("Not a square matrix. Can't be exponentiated")       
