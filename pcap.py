from scapy.all import *
import matplotlib.pyplot as plt

def main():

    # rdpcap comes from scapy and loads in our pcap file
    packets = rdpcap('D:/documents/users/ofirgru/Downloads/packets.pcap')
    status=0
    arr=[]
    times=[]
    # Let's iterate through every packet
    firstTime = int(str(packets[0].time).replace('.',''))
    for packet in packets:
    #     print(packet.getlayer('IP').)
    #     print(packet.getlayer('IP').display())
    #     print(packet.display())
        try:
            time=(int(str(packet.time).replace('.',''))-firstTime)/1000000
            # print((time))
            src = packet['IP'].src
            dst = packet['IP'].dst
            size = packet['IP'].len
            # print(size)
            if dst == '132.72.65.166':
                status += size
            else:
                status -= size
            # if dst == '132.72.65.166':
            #     status -= size

            arr.append(status)
            times.append(time)
        except:
            continue
    print(arr)
    print(times)
    # plt.plot(times, arr)
    plt.plot(times, arr)
    plt.show()

if __name__ == '__main__':
    main()