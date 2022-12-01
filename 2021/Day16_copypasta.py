version_sum = 0
def parse_packet(packet,depth):
    '''parse a binary packet
    packet is a string representation of binary
    (because I can handle strings better :) )
    returns a tuple (version,result,rest)
    version is the version, as an int (also added to version_sum)
    result: the resulting number
    rest: the part iof the input string that remains after one packet was parsed
    '''
    global version_sum

    # if the packet is all zeros, it's the padding
    if packet.find("1")==-1:
        print("zeros dropped")
        return(0,0,[],"")

#    if depth==0:
#        print(packet)

    s_version=packet[0:3]
    s_type=packet[3:6]
    s_rest=packet[6:]

    version=int(s_version,2)
    type=int(s_type,2)

    version_sum+=version

    if type==4:
        s_literal=""
        while s_rest:
            s_literal+=s_rest[1:5]
            q=s_rest[0]
            s_rest=s_rest[5:]
            if q=="0":
                break
        return (version,int(s_literal,2),s_rest)
    else:
        # first we parse, to find out the content on which to run the operator
        content=[]
        if s_rest[0]=="0":
            leng=int(s_rest[1:16],2)
            s_rest=s_rest[16:]
            s_subpackets=s_rest[:leng]
            s_rest=s_rest[leng:]
#            print("Length-based start:",leng,"at depth:",depth,"remaining bits:",len(s_rest))
            while s_subpackets:
#                print("Length-based ongoing:",len(s_subpackets),"at depth:",depth)
                t_version,t_content,s_subpackets=parse_packet(s_subpackets,depth+1)
                content.append(t_content)
#            print("Length-based completed at depth:",depth)
        else:
            num=int(s_rest[1:12],2)
#            print("Number-based start:",num,"at depth:",depth)
            s_rest=s_rest[12:]
            aa=list(range(num))
            for i in aa:
#                print("Number-based:",i,"at depth:",depth)
                #print(s_rest)
                t_version,t_content,s_rest=parse_packet(s_rest,depth+1)
                content.append(t_content)
        # now we handle the content based on the operator
        result=0 # just to define scope
        if type==0:
            result=sum(content)
        elif type==1:
            result=1
            for c in content:
                result*=c
        elif type==2:
            result=min(content)
        elif type==3:
            result=max(content)
        else:
            if len(content)!=2:
                print("Content length error")
            result=0
            if (type==5) and (content[0]>content[1]):
                result=1
            if (type==6) and (content[0]<content[1]):
                result=1
            if (type==7) and (content[0]==content[1]):
                result=1
        return(version,result,s_rest)

f = open("input/day16.txt").readlines()
s=f[0].strip()
top_packet=bin(int(s,16))[2:].zfill(len(s)*4)

# Testing infrastructure for short examples - comment out the above, uncomment this
#test_str="880086C3E88112"
#top_packet=bin(int(test_str,16))[2:].zfill(len(test_str)*4)

t_version,result,t_rest=parse_packet(top_packet,0)
print("Part 1:",version_sum)
print("Part 2:",result)
