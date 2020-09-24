import time
st_time = time.time()

m_list = [4,8,1,2,9,6,7,3,5]
for i in range(len(m_list)):
    for j in range(len(m_list)-1):
        if m_list[j] > m_list[j+1]:
            m_list[j],m_list[j+1] = m_list[j+1],m_list[j]
print(m_list)
 #to calcualte time           
end_time = time.time()
print("time required >  sec:-    ",end_time-st_time)





# *********After optimizing it ***************

v1 = time.time()

m_list = [4,8,1,2,9,6,7,3,5]
for i in range(len(m_list)-1,-1,-1):
    for j in range(i):
        if m_list[j] > m_list[j+1]:
            m_list[j],m_list[j+1] = m_list[j+1],m_list[j]
print(m_list)


v2 = time.time()
print("time required >  sec:-    ",v2-v1)