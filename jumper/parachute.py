class Parachute():
    def __init__(self):
        self._tries = 0

    def _get_tries(self):
        return self._tries

    def _set_tries(self):
        self._tries += 1

    def _set_parachute(self, tries):
        """
        Passes the current parachute to a caller outside the Parachute class
        """
        return self.draw(tries)

    def _draw(self, tries):
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