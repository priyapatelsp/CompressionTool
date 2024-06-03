import os
import heapq

class CompressionTool:
    def __init__(self,path):
        self.path=path
        self.heap=[]
        self.codes={}
        self.reverse_mapping={}

    class HeapNode:
        def __init__(self,char,freq):
            self.char=char
            self.freq=freq
            self.left=None
            self.right=None

        def __lt__(self,other):
            return self.freq<other.freq
        
        def __eq__(self, other):
            if(other==None):
                return False
            if(not isinstance(other,self.HeapNode)):
                return False
            return self.freq==other.freq
            

    def make_freq_dict(self,text):
        freq={}
        for char in text:
            if not char in freq:
                freq[char]=0
            freq[char]+=1
        return freq

    def make_heap(self,freq):
        for key in freq:
            node=self.HeapNode(key,freq[key])
            heapq.heappush(self.heap,node)
        

    def merge_code(self):
        while(len(self.heap)>1):
            node1=heapq.heappop(self.heap)
            node2=heapq.heappop(self.heap)
            merged= self.HeapNode(None,node1.freq+node2.freq)
            merged.left=node1
            merged.right=node2
            heapq.heappush(self.heap,merged)

    def make_codes_helper(self,node,curr_code):
        if(node==None):
            return 
        if(node.char!=None):
            self.codes[node.char]=curr_code
            self.reverse_mapping[curr_code]=node.char

        self.make_codes_helper(node.left,curr_code+"0")
        self.make_codes_helper(node.right,curr_code+"1")
    
    def make_code(self):
        root=heapq.heappop(self.heap)
        curr_code=""
        self.make_codes_helper(root,curr_code)

    def get_encoded_text(self,text):
        encoded_text=""
        for char in text:
            encoded_text+=self.codes[char]
        return encoded_text

    def pad_encoded_text(self,encoded_text):
        extra_padding = 8-len(encoded_text)%8
        for i in range(extra_padding):
            encoded_text+= "0"
        
        padded_info="{0:08b}".format(extra_padding)
        encoded_text=padded_info+encoded_text
        return encoded_text

    def get_byte_array(self,padded_encoded_text):
        b=bytearray()
        for i in range(0,len(padded_encoded_text),8):
            byte=padded_encoded_text[i:i+8]
            b.append(int(byte,2))
        return b
    
    def compress(self):
        filename,file_extension=os.path.splitext(self.path)
        out_path=filename+".bin"
        with open(self.path,'r') as file, open(out_path,'wb') as output:
            text=file.read() 
            text=text.rstrip()

            freq=self.make_freq_dict(text)

            self.make_heap(freq)
            self.merge_code()
            self.make_code()

            encoded_text=self.get_encoded_text(text)
            paded_encoded_text=self.pad_encoded_text(encoded_text)

            b=self.get_byte_array(paded_encoded_text)
            output.write(bytes(b))
        print("compressed::")
        return out_path

    def remove_padding(self,bit_string):
        padded_info=bit_string[:8]
        extra_padding=int(padded_info,2)

        bit_string=bit_string[8:]
        encoded_text=bit_string[:-1*extra_padding]
        return encoded_text


    def decode_text(self,encoded_text):
        current_code=""
        decoded_text=""
        for bit in encoded_text:
            current_code+=bit
            if(current_code in self.reverse_mapping):
                char=self.reverse_mapping[current_code]
                decoded_text+=char
                current_code=""
        return decoded_text



    def decompress(self,intput_path):
        filename,file_extension=os.path.splitext(intput_path)
        out_path=filename+"_decompressed" 

        with open(intput_path,'rb') as file,open(out_path,'w') as output:
            bit_string=""
            byte=file.read(1)
            while(len(byte)>0):
                byte=ord(byte)
                bits=bin(byte)[2:].rjust(8,'0')
                bit_string+=bits
                byte=file.read(1)
            encoded_text=self.remove_padding(bit_string)
            decoded_text=self.decode_text(encoded_text)

            output.write(decoded_text)

        print("decompressed")
        return out_path

        

    
