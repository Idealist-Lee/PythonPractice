import numpy as np
# L1 = np.array([1.,2,3,4,5])
# L2 = np.array([1,2,3,4,5])
# L2[0]=8.0
# L1[2]=5
# print(L1)
# print(L2)
# #
# L1 = np.array([1,2,3,4,5])
# print(L1)
# L1=L1.astype(float)
# print(L1)

# L2 = np.array([1, 2, 3, 4, 5])
# print(L2/1)
# print(L2)

# arr1=np.ones((1,5,5))
# print(arr1)
# print(arr1.shape)

# arr1 = np.arange(10)
# print(arr1)
# arr2 = arr1.reshape( (1,-1) )
# print(arr2)

# arr2 = np.arange(10).reshape(2,5)
# print(arr2)
# arr1 = arr2.reshape( -1 )
# print(arr1)

# arr1 = np.arange(10)
# print(arr1)

# arr1 = np.arange(1,10,4)
# print(arr1)

# arr1 = np.zeros( 3 )
# print(arr1)

# arr2 = np.ones( (1,3) )
# print(arr2)

# arr1 = np.random.random( 5 )
# print( arr1 )

# arr2 = np.random.randint( 10,100,(1,15) )
# print(arr2)

# arr3 = np.random.normal( 0,1,(2,3) )
# print( arr3 )

# arr4=np.random.randn(2,3)
# print(arr4)

# arr1 = np.arange(0,90,10)
# print(arr1)
# print( arr1[ [0,2] ] )

# arr2 = np.arange(1,17).reshape(4,4)
# print(arr2)
# print( arr2[ [0,1] , [0,1] ] )
# print( arr2[ [0,1,2] , [2,1,0] ] )

# arr2 = np.arange(1,21).reshape(4,5)
# print( arr2 )
# print('\n')
# # print( arr2[ 1:3 , 1:-1 ] )
# print( arr2[ ::3 , ::2 ] )

# arr5 = np.arange(1,16).reshape(3,5)
# print( arr5 )
# cut = arr5[ : , 2 ]
# # print( cut )
# print( '\n' )
# cut = cut.reshape( (-1,1) )
# print(cut)


# arr = np.arange(10)
# print(arr)
# cut = arr[ : 3 ]
# print(cut)
# cut[0] = 100
# print(cut)
# print(arr)


# arr = np.arange(10)
# print(arr)
# copy = arr[ : 3 ] .copy()
# print(copy)
# copy [0] = 100
# print(copy)
# print(arr)

# arr1 = np.arange(10)
# print(arr1)
# arr2 = arr1
# print(arr2)
# arr2[0] = 100
# print(arr2)
# print(arr1)

# arr1 = np.arange(1,4)
# print(arr1)
# arr2 = arr1.reshape( (1,-1) )
# print(arr2)
# arr3 = arr2.T
# print(arr3)


# arr1 = np.arange(10)
# print( arr1 )
# arr_ud = np.flipud(arr1)
# print( arr_ud )


# arr2 = np.arange(1,21).reshape(4,5)
# print( arr2 )
# print( '\n' )
# arr_lr = np.fliplr(arr2)
# print( arr_lr )
# print( '\n' )
# arr_ud = np.flipud(arr2)
# print( arr_ud )


# arr1 = np.array( [1,2,3] )
# print(arr1)
# arr2 = np.array( [4,5,6] )
# print(arr2)
# arr3 = np.concatenate( [arr1,arr2] )
# print(arr3)


# arr1 = np.array( [[1,2,3],[ 4,5,6]] )
# print(arr1)
# print( '\n' )
# arr2 = np.array( [[7,8,9],[10,11,12]] )
# print(arr2)
# print( '\n' )
# arr3 = np.concatenate( [arr1,arr2] )
# print(arr3)
# print( '\n' )
# arr4 = np.concatenate( [arr1,arr2] ,axis=1 )
# print(arr4)

# arr = np.arange(10,100,10)
# print(arr)
# print( '\n' )
# arr1,arr2,arr3 = np.split( arr , [2,8] )
# print(arr1)
# print(arr2)
# print(arr3)

# arr = np.arange(1,9).reshape(2,4)
# print(arr)
# print( '\n''\n' )
# arr1,arr2 = np.split(arr,[1])
# print(arr1  ,'\n', arr2)
# print( '\n' '\n')
# arr1,arr2,arr3 = np.split( arr , [1,3] , axis=1 )
# print( arr1 ,'\n''\n', arr2 ,'\n''\n', arr3 )

# arr1 = np.arange(-1,-9,-1).reshape(2,4)
# arr2 = -arr1
# print( arr1 )
# print( '\n' )
# print( arr2 )
# print( '\n' )
# print( arr1 + arr2 )
# print( '\n' )
# print( arr1 - arr2 )
# print( '\n' )
# print( arr1 * arr2 )
# print( '\n' )
# print( arr1 / arr2 )
# print( '\n' )
# print( arr1 ** arr2)

# arr1 = np.arange(3)
# print(arr1)
# print( '\n' )
# arr2 = np.arange(3).reshape(3,1)
# print(arr2)
# print( '\n' )
# print(arr1*arr2)

# arr1 = np.arange(10).reshape(5,2)
# print(arr1)
# print( '\n' )
# arr2 = np.arange(16).reshape(2,8)
# print(arr2)
# print( '\n' )
# print( np.dot(arr1,arr2) )


# arr_v = np.array( [-10, 0, 10] )
# abs_v = np.abs(arr_v)
# print( '原数组是：' , arr_v )
# print( '绝对值是：' , abs_v )
# theta = np.arange(3) * np.pi / 2
# sin_v = np.sin(theta)
# cos_v = np.cos(theta)
# tan_v = np.tan(theta)
# print( '原数组是：' , theta )
# print( '正弦值是：' , sin_v )
# print( '余弦值是：' , cos_v )
# print( '正切值是：' , tan_v )
# x = np.arange(1,4)
# print( 'x =' , x )
# print( 'e^x =' , np.exp(x) )
# print( '2^x =' , 2**x )
# print( '10^x = ' , 10**x )
# x = np.array( [1,10,100,1000] )
# print( 'x =' , x )
# print( 'ln(x) =' , np.log(x) )
# print( 'log2(x) =' , np.log(x) / np.log(2) )
# print( 'log10(x) =' , np.log(x) / np.log(10) )


# # 最大值函数 np.max( )与最小值函数 np.min( )
# arr = np.random.random((2,3))
# print( arr )
# print( '按维度一求最大值：' , np.max(arr,axis=0) )
# print( '按维度二求最大值：' , np.max(arr,axis=1) )
# print( '整体求最大值：' , np.max(arr) )
#
# # 求和函数 np.sum( )与求积函数 np.prod( )
# arr = np.arange(10).reshape(2,5)
# print( arr )
# print( '按维度一求和：' , np.sum(arr,axis=0) )
# print( '按维度二求和：' , np.sum(arr,axis=1) )
# print( '整体求和：' , np.sum(arr) )
#
# # 均值函数 np.mean( )与标准差函数 np.std( )
# arr = np.arange(10).reshape(2,5)
# print( arr )
# print( '按维度一求平均：' , np.mean(arr,axis=0) )
# print( '按维度二求平均：' , np.mean(arr,axis=1) )
# print( '整体求平均：' , np.mean(arr) )


# arr1 = np.arange(1,6)
# arr2 = np.flipud(arr1)
# print(arr1)
# print(arr2)
# print( arr1 > arr2)


# arr = np.random.normal( 0,1,10000 )
# num = np.sum( np.abs(arr) < 1 )
# print( num )


# arr1 = np.arange(1,10)
# arr2 = np.flipud(arr1)
# print(arr1)
# print(arr2)
# print( np.any( arr1 == arr2 ) )

#
# arr = np.random.normal( 500,70,100000 )
# print( np.all( arr > 250 ) )


# arr1 = np.arange(1,10)
# arr2 = np.flipud(arr1)
# print(arr1)
# print(arr2)
# print( arr1 > arr2)
# print( arr1[ arr1 > arr2 ] )
# print( arr2[ arr1 > arr2 ] )


arr = np.random.normal( 500,70,1000)
print( np.where( arr > 650 )[0] )
print( np.where( arr == np.max(arr) )[0] )