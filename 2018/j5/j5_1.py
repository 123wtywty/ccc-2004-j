pages = 3
page_list = [[3, 2, 3], [0], [2,4], [2]]


story_lines = []


story_line = []


def get_line(i, page_list, story_line = []):

    #print(i)
    story_line.append(i)


    for ii in page_list[i-1]:
        #print('ii', ii)
        #story_line.append(ii)

        if ii == 0:
            #print('r')
            story_line.append(ii)
            print(story_line)

            return story_line
            #get_line(i, page_list, story_line=[])

        else:
            print('else')
            res = get_line(ii, page_list, story_line)
            print('res', res)



#for i in page_list[0]:
    #print(get_line(i, page_list))


#for i in get_line(1, page_list):
    #print(i)
print(get_line(1, page_list))

