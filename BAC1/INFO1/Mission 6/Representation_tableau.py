def table(file_in,file_out,width):
     with open(file_in,"r") as file:
         out = "+" + (width+2)*"-" + "+\n"
         fi = file.readlines()
         for i in range(len(fi)):
             fi[i] = fi[i].strip("\n")
             fi[i] += width*" "
     for i in fi:
         out += "| " + i[:width] + " |\n"
     out += "+" + (width+2)*"-" + "+"
     with open(file_out,"w") as file:
         return file.write(out)

print(table("file_in.txt","file_out.txt",4))