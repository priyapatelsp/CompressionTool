import os

class HuffmanCoding:
    def __init__(self,path):
        self.path=path
        self.heap=[]
        self.codes={}

    class HeapNode:
        def __init__(self,char,freq):
            self.char=char
            self.freq=freq
            

    def make_freq_dict(text):
        freq={}
        for char in text:
            if not char in freq:
                freq[char]=0
            freq[char]+=1
        return freq

    def make_heap(self,freq):
        #make priority ques

    def merge_code(self):
        #dedje
    
    def make_code(self):
        #jdkf

    def get_encoded_text(self,text):

    def pad_encoded_text(self,encoded_text):

    def get_byte_array(self,padded_encoded_text):

    def compress(self):
        filename,file_extension=os.path.splittext(self.path)
        out_path=filename+".bin"

        with open(self.path,'r') as file, open(out_path,'wb') as output:
            text=file.read() 
            text=text.rstrip()

            freq=make_freq_dict(text)

            self.make_heap(freq)
            self.merge_code()
            self.make_code()

            encoded_text=get_encoded_text(text)
            paded_encoded_text=pad_encoded_text(encoded_text)

            b=self.get_byte_array(paded_encoded_text)
            output.write(bytes(b))
        print("compressed::")
        return out_path


        

    
