import common
import numpy as np
import functools
from enum import Enum
from datetime import datetime

from common import read_file

daynum = 16 # set to number

class PacketType(Enum):
    SUM = 0
    PROD = 1
    MIN = 2
    MAX = 3
    LIT = 4
    GT = 5
    LT = 6
    EQ = 7



class Packet:
    def __init__(self, version, ptype):
        self.sub_packets = []
        self.version = version 
        self.ptype = ptype
        self.value = 0
        self.length_id = -1
        self.num_packets = 0
        self.total_packets_len = 0

    def __str__(self):
        return f'value: {self.value}, version: {self.version}, type: {self.ptype}, sub_packets = {len(self.sub_packets)}'

    def add_sub_packet(self, packet):
        self.sub_packets.append(packet)

    def calculate_packet_value(self):
        if len(self.sub_packets) > 0:
            if ptype == PacketType.SUM:
                self.value = sum([p.value for p in self.sub_packets])        

            elif ptype == PacketType.PROD:
                self.value = np.prod([p.value for p in self.sub_packets])        

            elif ptype == PacketType.MIN:
                self.value = min([p.value for p in self.sub_packets])        

            elif ptype == PacketType.MAX:
                self.value = max([p.value for p in self.sub_packets])        

            elif ptype == PacketType.GT:
                self.value = 1 if self.sub_packets[0] > self.sub_packets[1] else 0

            elif ptype == PacketType.LT:
                self.value =  1 if self.sub_packets[0] < self.sub_packets[1] else 0

            elif ptype == PacketType.EQ:
                self.value =  1 if self.sub_packets[0] == self.sub_packets[1] else 0
        return -1

def interpret_input(input_text):
    binstr = ''
    for c in input_text[0]:
        binstr += bin(int(c,16))[2:].zfill(4)
        
    return binstr


def compute_literal_value(binstr):
    num = ''
    counter = 0
    for i in range(0, len(binstr), 5):
        counter += 1
        group = binstr[i:i+5]
        num += group[1:]
        if(group[0] == '0'):
            break
    return (counter, num)

def part1(binstr):
    remainder = binstr
    packets = []
    while(len(remainder) > 6):
        version = int(remainder[0:3],2)
        ptype = int(remainder[3:6],2)
        remainder = remainder[6:]
        packet = Packet(version, ptype)
        # print(packet)
        if ptype == 4:
            counter, num = compute_literal_value(remainder) 
            remainder = remainder[(counter * 5):]
        else:
            length_type_id = remainder[0]
            remainder = remainder[1:]
            if length_type_id == '0':
                remainder = remainder[15:]
            else:
                remainder = remainder[11:]
        packets.append(packet)
    return packets

def calc_sample():
    samples = [['8A004A801A8002F478'], ['620080001611562C8802118E34'], ['C0015000016115A2E0802F182340'], ['A0016C880162017C3686B18A3D4780']]
    expected_results = [16,12,23,31]
    bin_strings = []
    for sample in samples:
        bin_strings.append(interpret_input(sample))
        
    for i, binstr in enumerate(bin_strings):
        interpreted_bin = part1(binstr)
        result = sum([int(x.version) for x in interpreted_bin])
        assert result == expected_results[i], f'Expected {expected_results[i]}, found {result}'

def get_main_packet(binstr):
    version = int(binstr[0:3],2)
    ptype = int(binstr[3:6],2)
    remainder = binstr[6:]

    if ptype != 4:
        packet = Packet(version, ptype)
        return (packet, remainder[1:])
    else:
        print('whoops')

def iterate_sub_packets(main_packet):
    outer_packet, remainder = main_packet
    length_id = int(outer_packet.length_id)

    if length_id == 0:
        total_length = int(remainder[0:15],2)
        test = remainder.copy()[15:]
        remainder = remainder[15:15+total_length]
        print(len(test))
        print(len(remainder))
        

    elif length_id == 1:
        num_packets = int(remainder[0:11],2)
        remainder = remainder[11:]
        
def recurse_test(current_packet, remainder):
    version = int(remainder[0:3],2)
    ptype = PacketType(int(remainder[3,6],2))
    remainder = remainder[6:]

    if ptype == PacketType.LIT:
       packet = Packet(version, ptype)
       counter, packet.value = compute_literal_value(remainder)
       current_packet.add_sub_packet(packet)
       current_packet.calculate_packet_value()
       return current_packet
    else:
        length_id = int(remainder[0])
        packet = Packet(version, ptype)
        current_packet.add_sub_packet(packet)
        if length_id == 0:
            total_length = int(remainder[0:15],2)
            test = remainder.copy()[15:]
            remainder = remainder[15:15+total_length]
            print(len(test))
            print(len(remainder))
        elif length_id == 1:
            num_packets = int(remainder[0:11],2)
            remainder = remainder[11:]
            
        else:
            print('not supposed to be here')
            return current_packet
            
        
       
# 101 000 1 00000110101 10110011101000
    
    
# 110 000 1 00000000010 110 100 00001 010 100 00010 = 1 + 2
# 000 001 0 000000000010110 10110000110011100010010000
# 100 010 0 0000000001000011011000011111010001000000100010010
# 110 011 1 0000000001100010000111101100010000001000100100000
# 110 110 0 00000000001011010110000101010100011110000
# 111 101 1 000000000101111000010110110001111
# 100 111 0 00000000001011010110000101111100011110000
# 100 111 0 0000000010100000100001000000000100101000000110010000011110001100000000010000100000100101000001000

def p2_sample():
    samples = [['C200B40A82'], ['04005AC33890'], ['880086C3E88112'], ['CE00C43D881120'], ['D8005AC2A8F0'],
        ['F600BC2D8F'], ['9C005AC2F8F0'], ['9C0141080250320F1802104A08']]
    expected_results = [3, 54, 7,8,1,0,0,1]
    bin_strings = []
    for sample in samples:
        bin_strings.append(interpret_input(sample))

    main_packet = get_main_packet(bin_strings[0])
    subs = iterate_sub_packets(main_packet)
        
    # for i, binstr in enumerate(bin_strings):
    #     interpreted_bin = part1(binstr)
        # result = sum([int(x.version) for x in interpreted_bin])
        # assert result == expected_results[i], f'Expected {expected_results[i]}, found {result}'
    
def calc_p1(binstr):
    interpreted_bin = part1(binstr)
    result = sum([int(x.version) for x in interpreted_bin])
    return result

starttime = datetime.now()

day_sample = read_file(f'input/day{daynum}_sample.txt')
day_input = read_file(f'input/day{daynum}.txt')

sample = interpret_input(day_sample)
day = interpret_input(day_input)

# p1s = calc_sample()
# # print(p1s)
# print(f"Time taken: {datetime.now() - starttime}")

# p1 = calc_p1(day)
# print(p1)
# print(f"Time taken: {datetime.now() - starttime}")

p2s = p2_sample()
print(f"Time taken: {datetime.now() - starttime}")

# p2 = calc(day)
# print(p2)
# print(f"Time taken: {datetime.now() - starttime}")


versions = ['000','001', '010', '011', '100', '101', '110', '111']
sum_type = '000'
lit_type = '100'
len1 = '00000000001'
len2 = '00000000010'
num2 = '00010'
num3 = '00011'
num17 = '1000100001' # = 00010001

lit_2 = versions[2] + lit_type + num2
sum_2 = sum_type + '1' + len2
sum_1 = sum_type + '1' + len1


main_packet = versions[0] + sum_2
sub_packet1 = versions[1] + sum_1 + lit_2
sub_packet2 = versions[3] + sum_2 + versions[4] + sum_2 + lit_2 + versions[5] + lit_type + num3 + sum_1 + versions[6] + lit_type + num17

binstr = main_packet + sub_packet1 + sub_packet2

print(binstr)

version = int(binstr[0:3],2)
ptype = PacketType(int(binstr[3:6],2))
packet = Packet(version, ptype)
packet.length_id = int(binstr[6],2)
packet.num_packets = int(binstr[7:18],2)

def R(binstr, packet, total_sum):
    print(len(binstr))
    
    if(len(binstr) < 6):
        return total_sum
    else:
    
        version = int(binstr[0:3],2)
        ptype = PacketType(int(binstr[3:6],2))
        p = Packet(version, ptype)
        binstr = binstr[6:]
    
            
        if(ptype == PacketType.LIT):
            counter, num = compute_literal_value(binstr)
            p.value = int(num,2)
            packet.add_sub_packet(p)
            R(binstr[counter*5:], packet, total_sum + p.value)
        else:
            p.length_id = int(binstr[0],2)
            p.num_packets = int(binstr[1:12],2)
            for num in range(p.num_packets):
                if(packet is not None):
                    packet.add_sub_packet(p)
                R(binstr[12:], p, total_sum)
        return total_sum


# x = R(binstr[6:], None, 0)
# print(x)




def manual_run(binstr):
    packet = Packet(int(binstr[0:3],2), PacketType(int(binstr[3:6],2)))
    binstr = binstr[6:]

    print(packet)

    if(ptype != PacketType.LIT):
        packet.length_id = int(binstr[0])
        binstr = binstr[1:]
        print(packet.length_id)
        if(packet.length_id == 0):
            packet.total_packets_len= int(binstr[:15],2)
            binstr = binstr[15:]
            binstr = binstr[packet.total_packets_len:]
        else:
            packet.num_packets = int(binstr[:11],2)
            print(f'num pack: {packet.num_packets}')
            binstr = binstr[11:]
            for i in range(packet.num_packets):
                p = Packet(int(binstr[0:3],2), PacketType(int(binstr[3:6],2)))
                print(f'p: {p}')
                binstr = binstr[6:]

                if(p.ptype == PacketType.LIT):
                    counter, num = compute_literal_value(binstr)
                    binstr = binstr[counter*5:]
                    p.value = int(num,2) 
                else:
                    p.length_id = int(binstr[6])
                    print(f'p len id: {p.length_id}')
                    binstr = binstr[6:]
                    if(p.length_id == 0):
                        p.total_packets_len= int(binstr[:15],2)
                        binstr = binstr[15:]
                        binstr = binstr[p.total_packets_len:]
                    else:
                        p.num_packets = int(binstr[:11],2)
                        binstr = binstr[11:]
                        for i in range(p.num_packets):
                            p2 = Packet(int(binstr[0:3],2), PacketType(int(binstr[3:6],2)))
                            binstr = binstr[6:]
                            
                            if(p2.ptype == PacketType.LIT):
                                counter, num = compute_literal_value(binstr)
                                binstr = binstr[counter*5:]
                                p2.value = int(num,2) 
                            else:
                                p2.value = 99
                            p.add_sub_packet(p2)
                packet.add_sub_packet(p)
                p.calculate_packet_value
            packet.calculate_packet_value
    return packet
                                
# 000 000 1 00000000010 | 001 000 1 00000000001 | 010 100 00010 | 011 000 1 00000000010 | 10000010000000001001010000010101100000110001000000000011101001000100001
def process_inner(binstr):
    p = Packet(1,PacketType.LIT)
    p.value = 2
    return [p]

def process_inner_2(binstr, main_packet):
    while(len(binstr) > 6):
        packet = Packet(int(binstr[0:3],2), PacketType(int(binstr[3:6],2)))
        binstr = binstr[6:]
        if(packet.ptype == PacketType.LIT):
            counter,num = compute_literal_value(binstr)
            packet.value = int(num,2)
            binstr = binstr[counter*5:]
        else:
            length_type_id = binstr[0]
            packet.length_id = length_type_id
            remainder = binstr[1:]
            if length_type_id == '0':
                total_length = int(binstr[:15], 2)
                remainder = binstr[15:]
                packets = process_inner(binstr)
                packet.total_packets_len = total_length
                packet.sub_packets = packets
                remainder = binstr[total_length:]
            else:
                num_packets = int(binstr[:11],2)
                remainder = binstr[11:]
                for i in range(num_packets):
                    p = Packet(int(binstr[0:3],2), PacketType(int(binstr[3:6],2)))
                    remainder = binstr[6:]
                    plength, packets = process_inner_2(binstr, main_packet)
                    p.sub_packets = packets
                    packet.add_sub_packet(p)
        main_packet.add_sub_packet(packet)
        return 0, main_packet
        

def part2_try(binstr):
    remainder = binstr
    while(len(remainder) > 6):
        version = int(remainder[0:3],2)
        ptype = int(remainder[3:6],2)
        remainder = remainder[6:]
        packet = Packet(version, ptype)
        # print(packet)
        if ptype == 4:
            counter, num = compute_literal_value(remainder) 
            remainder = remainder[(counter * 5):]
            packet.value = int(num,2)
        else:
            length_type_id = remainder[0]
            packet.length_id = length_type_id
            remainder = remainder[1:]
            if length_type_id == '0':
                total_length = int(remainder[:15], 2)
                remainder = remainder[15:]
                packets = process_inner(remainder)
                packet.total_packets_len = total_length
                packet.sub_packets = packets
                remainder = remainder[total_length:]
            else:
                num_packets = int(remainder[:11],2)
                remainder = remainder[11:]
                for i in range(num_packets):
                    p = Packet(int(remainder[0:3],2), PacketType(int(remainder[3:6],2)))
                    remainder = remainder[6:]
                    plength, p = process_inner_2(binstr,p)
                    packet.add_sub_packet(p)
    return packets

print(part2_try(binstr))
