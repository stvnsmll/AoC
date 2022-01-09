#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 31.12.21              #
#                       #
# Day 16, Part 1        #
#########################

from datetime import datetime


def aoc2021_16_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 16, Part 1\n~~ running as a test ~~")

    startTime = datetime.now()

    # Using readline()
    input_data_file = open(filename, 'r')
    input_data = []
    while True:
        # Get next line from file
        line = input_data_file.readline()
        # if line is empty end of file is reached
        if not line:
            break
        #print(line)
        input_data.append(line.strip())
    input_data_file.close()

    print(input_data)
    binaryFull = ""
    for char in input_data[0]:
        #print(char, end=": ")
        binarychar = "{0:04b}".format(int(char, 16))
        binaryFull += binarychar
        #print(binarychar)
    print()
    #binaryFull = "0101001000100100"
    print(binaryFull)

    [total_versions, remaining_bits, packet_length] = decode_packet2(binaryFull)
    print()
    print(f"Sum of versions: {total_versions}")
    print(f"  remaining bits: {remaining_bits}")
    
    answer = total_versions
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer


def decode_literal(literal_binary_packet):
    #literal value
    integer_binary = ""
    #in groups of 5 characters, check char #1. if == 1, it's not the last packet and keep appending.
    # if == 0, it's the last packet. terminate there and count trailing 0s until the full packet is a 
    # multiple of 4
    exit_loop = 0
    start_loc = 0
    loop_count = 0
    while exit_loop == 0:
        loop_count += 1
        if literal_binary_packet[start_loc] == "0":
            #print("exit now")
            exit_loop = 1
        to_add = literal_binary_packet[start_loc + 1:start_loc + 5]
        #print(to_add)
        integer_binary += literal_binary_packet[start_loc + 1:start_loc + 5]
        start_loc += 5
    packet_length = (6 + len(integer_binary) + loop_count)
    #print(f"  Packet length: {packet_length}")
    #print(f"  Binary literal value: {integer_binary}")
    literal_value = int(integer_binary, 2)
    #print(f"  Integer literal value: {literal_value}")
    return [literal_value, packet_length]

def decode_packet(fullpacket, extra_offset):
    print(f"Starting a packet decode on string: \n{fullpacket}")
    if len(fullpacket) < 8:
        return [0, 0]
    versionsum = 0
    offsettotal = 0
    version = int(fullpacket[0:3], 2)
    versionsum += version
    typeID = int(fullpacket[3:6], 2)
    print(f"Ver: {version}, Type ID: {typeID}")
    if typeID == 4:
        #this is a literal evaluation
        start_loc = 6#offset it by 6 for the headed information
        literal_binary_content = fullpacket[start_loc:]
        [literal_value, packet_length] = decode_literal(literal_binary_content)
        print(f"  Packet length: {packet_length} (length to offset if nested)")
        print(f"  Integer literal value: {literal_value}")
        offsettotal += packet_length
    else:
        #this is an operator
        lengthID = int(fullpacket[6], 2)
        print(f"  Length type ID: {lengthID}")
        if lengthID == 0:
            #next 15 bits converted to integer is the length in bits of the sub-packets
            start_loc = 7 + extra_offset
            sub_packet_bits = fullpacket[start_loc:start_loc + 15]
            sub_packet_len = int(sub_packet_bits, 2)
            #print(fullpacket[start_loc + 15:])
            print(f"  Length of all sub-packets: {sub_packet_len}")
            offset = 0
            exit = 0
            while exit == 0:
                [versions, new_offset] = decode_packet(fullpacket[start_loc + 15 + offset:], 0)
                sub_packet_len -= new_offset
                print(f"  Remaining length: {sub_packet_len}")
                offset += new_offset
                versionsum += versions
                if sub_packet_len < 7:
                    exit = 1
            print(f"\nTotal Offset: {offset + extra_offset}")
            offsettotal = sub_packet_len + offset
        elif lengthID == 1:
            #next 11 bits converted to integer is the number of sub-packets
            start_loc = 7 + extra_offset
            sub_packetcount_bits = fullpacket[start_loc:start_loc + 11]
            sub_packets_count = int(sub_packetcount_bits, 2)
            print(f"  Sub-packet count: {sub_packets_count}")
            remaining_bits = fullpacket[start_loc + 11:]
            offset = 0
            for k in range(sub_packets_count):
                print(f"\nPacket # {k + 1}")
                print(f" offset is: {offset}")
                remaining_bits = remaining_bits[offset:]
                [versions, new_offset] = decode_packet(remaining_bits[offset:], 0)
                print(f"Finished a loop of the 'type 1' counts. full offset = {new_offset}")
                print(f"remaining bits: {remaining_bits[offset+new_offset:]}")
                versionsum += versions
                offset += new_offset
    return [versionsum, offsettotal]


def decode_packet2(remaining_bits):
    print(f"Starting a packet decode (v2) on string: \n{remaining_bits}")
    if len(str(remaining_bits)) < 8:
        return [0,0,4000]
    versionsum = 0
    version = int(remaining_bits[0:3], 2)
    versionsum += version
    typeID = int(remaining_bits[3:6], 2)
    print(f"Ver: {version}, Type ID: {typeID}")
    if typeID == 4:
        #this is a literal evaluation
        literal_binary_content = remaining_bits[6:]
        [literal_value, packet_length] = decode_literal(literal_binary_content)
        print(f"  Packet length: {packet_length} (length to offset if nested)")
        print(f"  Integer literal value: {literal_value}")
        remaining_bits = remaining_bits[packet_length:]
        print(f"  Remaining bits: {remaining_bits}")
    else:
        #this is an operator
        lengthID = int(remaining_bits[6], 2)
        print(f"  Length type ID: {lengthID}")
        if lengthID == 0:
            #next 15 bits converted to integer is the length in bits of the sub-packets
            sub_packet_len = int(remaining_bits[7:(7 + 15)], 2)
            print(f"  LenID = 0, sub-packet length: {sub_packet_len}")
            #trim the remaining bits...
            remaining_bits = remaining_bits[(7 + 15):]
            #print(remaining_bits)
            total_offsets = 0
            exit = 0
            while exit == 0:
                [versions, remaining_bits, new_offset] = decode_packet2(remaining_bits)
                total_offsets += new_offset
                versionsum += versions
                print(f"  total_offsets =  {total_offsets}")
                print(f"  sub_packet_len =  {sub_packet_len}")
                if total_offsets >= sub_packet_len:
                    exit = 1
            packet_length = (7 + 15 + sub_packet_len)#remaining_bits[(7 + 15 + sub_packet_len):]
        elif lengthID == 1:
            #next 11 bits converted to integer is the number of sub-packets
            sub_packets_count = int(remaining_bits[7:(7 + 11)], 2)
            print(f"  LenID = 1, number of sub-packets: {sub_packets_count}")
            remaining_bits = remaining_bits[(7 + 11):]
            print(remaining_bits)
            total_offsets = 0
            for k in range(sub_packets_count):
                print(k)
                [versions, remaining_bits, new_offset] = decode_packet2(remaining_bits)
                versionsum += versions
                total_offsets += new_offset
            packet_length = total_offsets
    return [versionsum, remaining_bits, packet_length]


if __name__ == "__main__":
   aoc2021_16_1("input.txt")