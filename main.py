import start
import lexer
import parser
import semantic
import treeGenerator
import assembler
import output

print("""
         ██████╗ ██████╗  █████╗  ██████╗██╗ █████╗ ███████╗██╗
        ██╔════╝ ██╔══██╗██╔══██╗██╔════╝██║██╔══██╗██╔════╝██║
        ██║  ███╗██████╔╝███████║██║     ██║███████║███████╗██║
        ██║   ██║██╔══██╗██╔══██║██║     ██║██╔══██║╚════██║╚═╝
        ╚██████╔╝██║  ██║██║  ██║╚██████╗██║██║  ██║███████║██╗
         ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝
""")


print("""
                              ██                                          
                            ██░░██                                        
                            ██░░██▒▒                                      
                          ██░░░░▒▒██                                      
                          ██░░░░▒▒▓▓                                      
                    ██████░░░░░░▒▒██                                      
                  ██░░░░░░██░░▒▒▓▓░░                                      
                ██░░░░░░░░▒▒░░▒▒▓▓░░                                      
            ████░░░░██░░░░░░░░▒▒▓▓░░                                      
          ██░░░░░░░░░░░░░░░░░░▒▒▓▓░░                                      
          ██░░░░░░░░░░░░▒▒░░░░▒▒▒▒▒▒                                      
            ████▒▒▒▒▒▒▒▒██░░▒▒██░░                                        
                ████████▒▒░░▒▒██                                          
                      ██▒▒░░░░▒▒▓▓                                        
                      ██▒▒░░░░░░▒▒██                                      
                    ██░░░░░░░░░░░░▒▒██                                    
                    ██░░░░▒▒██░░▒▒▒▒░░██████                              
                    ██░░░░▒▒▒▒██▒▒▒▒▒▒░░░░░░██████                        
                    ██░░██░░▒▒██▒▒▒▒░░░░░░░░░░░░░░████                    
                      ██░░░░▒▒██▒▒░░░░░░░░░░░░░░░░░░▒▒██                  
                      ██▒▒████▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒██                
                      ████▒▒▒▒░░░░░░██░░░░░░░░░░░░░░░░▒▒██                
                    ██████▒▒░░░░░░██▒▒░░░░░░░░░░░░░░░░░░▒▒██              
                    ██    ██▒▒░░░░██▒▒░░░░░░░░░░░░░░░░░░▒▒██              
                      ██    ██▒▒▒▒▓▓░░░░░░░░░░░░░░▒▒░░░░▒▒██              
                              ██████▒▒░░░░░░░░░░▒▒██░░░░▒▒██              
                                  ██▒▒░░░░░░░░░░▓▓██░░▒▒░░▒▒              
                                  ██▒▒░░░░░░▒▒██      ██▒▒░░██            
                                    ██▒▒░░▒▒██        ██▒▒░░██            
                                      ██▒▒▒▒██          ██▒▒██          
                                        ██▒▒██            ██▒▒██          
                                    ██████▒▒██              ██▒▒██      ██
                                  ██▒▒▒▒▒▒▒▒██                ██████████  
                                  ░░████████                              
""")
