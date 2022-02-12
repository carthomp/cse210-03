class Parachute():
    def __init__(self):
        self.tries = 0

    def get_tries(self):
        return self.tries

    def set_tries(self):
        self.tries += 1

    def set_parachute(self, tries):
        """
        Passes the current parachute to a caller outside the Parachute class
        """
        return self.draw(tries)

    def draw(self, tries):
        stages = [  # initial state 
                    """
                            ___                  
                           /___\\
                           \   /
                            \ /
                             O
                            \|/
                             |
                            / \\
                            
                         ********
                    
                    """,
                    # second state
                    
                    """
                                            
                           /___\\
                           \   /
                            \ /
                             O
                            \|/
                             |
                            / \\
                            
                        ********
                    """,

                    # third state
                    """
                        
                           \   /
                            \ /
                             O
                            \|/
                             |
                            / \\
                    
                        ********
                    """,

                    # fourth guess
                    """
                        
                            \ /
                             O
                            \|/
                             |
                            / \\
                        
                        ********
                    
                    """,

                    # you lost
                    """
                        
                             x
                            \|/
                             |
                            / \\
                    
                        ********
                    """
        ]
        return stages[tries]