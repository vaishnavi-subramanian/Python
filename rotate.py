def rotate(list):
    first=list[0]
    for i in range(len(list)):
        list[i-1]=list[i]
    list[len[list-1]]=first
list=["a","b","c"]
print("Before rotate %{list}")
rotate(list)


print("After rotate %{list}")
