from __future__ import division                                 
import numpy as np                                              
from pysd import functions                                      
from pysd import builder                                        
                                                                
class Components(builder.ComponentClass):                       
                                                                
    def input_delay_adjustment_time_flow_1_of_4(self):
        """Type: Flow or Auxiliary
        """
        return self.input() 

    def input_delay_adjustment_time_flow_2_of_4(self):
        """Type: Flow or Auxiliary
        """
        return self.input_delay_adjustment_time_stock_1_of_3()/(1.*self.adjustment_time()/3) 

    def input_delay_adjustment_time_flow_3_of_4(self):
        """Type: Flow or Auxiliary
        """
        return self.input_delay_adjustment_time_stock_2_of_3()/(1.*self.adjustment_time()/3) 

    def input_delay_adjustment_time_flow_4_of_4(self):
        """Type: Flow or Auxiliary
        """
        return self.input_delay_adjustment_time_stock_3_of_3()/(1.*self.adjustment_time()/3) 

    def dinput_delay_adjustment_time_stock_1_of_3_dt(self):                       
        return self.input_delay_adjustment_time_flow_1_of_4() - self.input_delay_adjustment_time_flow_2_of_4()                           

    def input_delay_adjustment_time_stock_1_of_3_init(self):                      
        return 0 * (self.adjustment_time() / 3)                           

    def input_delay_adjustment_time_stock_1_of_3(self):                            
        """ Stock: input_delay_adjustment_time_stock_1_of_3 =                      
                 self.input_delay_adjustment_time_flow_1_of_4() - self.input_delay_adjustment_time_flow_2_of_4()                          
                                             
        Initial Value: 0 * (self.adjustment_time() / 3)                    
        Do not overwrite this function       
        """                                  
        return self.state["input_delay_adjustment_time_stock_1_of_3"]              
                                             
    def dinput_delay_adjustment_time_stock_2_of_3_dt(self):                       
        return self.input_delay_adjustment_time_flow_2_of_4() - self.input_delay_adjustment_time_flow_3_of_4()                           

    def input_delay_adjustment_time_stock_2_of_3_init(self):                      
        return 0 * (self.adjustment_time() / 3)                           

    def input_delay_adjustment_time_stock_2_of_3(self):                            
        """ Stock: input_delay_adjustment_time_stock_2_of_3 =                      
                 self.input_delay_adjustment_time_flow_2_of_4() - self.input_delay_adjustment_time_flow_3_of_4()                          
                                             
        Initial Value: 0 * (self.adjustment_time() / 3)                    
        Do not overwrite this function       
        """                                  
        return self.state["input_delay_adjustment_time_stock_2_of_3"]              
                                             
    def dinput_delay_adjustment_time_stock_3_of_3_dt(self):                       
        return self.input_delay_adjustment_time_flow_3_of_4() - self.input_delay_adjustment_time_flow_4_of_4()                           

    def input_delay_adjustment_time_stock_3_of_3_init(self):                      
        return 0 * (self.adjustment_time() / 3)                           

    def input_delay_adjustment_time_stock_3_of_3(self):                            
        """ Stock: input_delay_adjustment_time_stock_3_of_3 =                      
                 self.input_delay_adjustment_time_flow_3_of_4() - self.input_delay_adjustment_time_flow_4_of_4()                          
                                             
        Initial Value: 0 * (self.adjustment_time() / 3)                    
        Do not overwrite this function       
        """                                  
        return self.state["input_delay_adjustment_time_stock_3_of_3"]              
                                             
    def smooth3_output(self):
        """Type: Flow or Auxiliary
        """
        return self.input_delay_adjustment_time_flow_4_of_4() 

    def smooth_n_output(self):
        """Type: Flow or Auxiliary
        """
        return SMOOTH N(Input, Adjustment Time , 0 , 5 ) 

    def smooth_output(self):
        """Type: Flow or Auxiliary
        """
        return SMOOTH(Input, Adjustment Time ) 

    def smoothi_output(self):
        """Type: Flow or Auxiliary
        """
        return SMOOTHI(Input, Adjustment Time, 0 ) 

    def adjustment_time(self):
        """Type: Flow or Auxiliary
        """
        return 2 

    def input_smooth_adjustment_time_flow_1_of_3(self):
        """Type: Flow or Auxiliary
        """
        return (self.input() - self.input_smooth_adjustment_time_stock_1_of_3()) / (1.*self.adjustment_time()/3) 

    def input_smooth_adjustment_time_flow_2_of_3(self):
        """Type: Flow or Auxiliary
        """
        return (self.input_smooth_adjustment_time_stock_1_of_3() - self.input_smooth_adjustment_time_stock_2_of_3())/(1.*self.adjustment_time()/3) 

    def input_smooth_adjustment_time_flow_3_of_3(self):
        """Type: Flow or Auxiliary
        """
        return (self.input_smooth_adjustment_time_stock_2_of_3() - self.input_smooth_adjustment_time_stock_3_of_3())/(1.*self.adjustment_time()/3) 

    def dinput_smooth_adjustment_time_stock_1_of_3_dt(self):                       
        return self.input_smooth_adjustment_time_flow_1_of_3()                           

    def input_smooth_adjustment_time_stock_1_of_3_init(self):                      
        return 0                            

    def input_smooth_adjustment_time_stock_1_of_3(self):                            
        """ Stock: input_smooth_adjustment_time_stock_1_of_3 =                      
                 self.input_smooth_adjustment_time_flow_1_of_3()                          
                                             
        Initial Value: 0                     
        Do not overwrite this function       
        """                                  
        return self.state["input_smooth_adjustment_time_stock_1_of_3"]              
                                             
    def dinput_smooth_adjustment_time_stock_2_of_3_dt(self):                       
        return self.input_smooth_adjustment_time_flow_2_of_3()                           

    def input_smooth_adjustment_time_stock_2_of_3_init(self):                      
        return 0                            

    def input_smooth_adjustment_time_stock_2_of_3(self):                            
        """ Stock: input_smooth_adjustment_time_stock_2_of_3 =                      
                 self.input_smooth_adjustment_time_flow_2_of_3()                          
                                             
        Initial Value: 0                     
        Do not overwrite this function       
        """                                  
        return self.state["input_smooth_adjustment_time_stock_2_of_3"]              
                                             
    def dinput_smooth_adjustment_time_stock_3_of_3_dt(self):                       
        return self.input_smooth_adjustment_time_flow_3_of_3()                           

    def input_smooth_adjustment_time_stock_3_of_3_init(self):                      
        return 0                            

    def input_smooth_adjustment_time_stock_3_of_3(self):                            
        """ Stock: input_smooth_adjustment_time_stock_3_of_3 =                      
                 self.input_smooth_adjustment_time_flow_3_of_3()                          
                                             
        Initial Value: 0                     
        Do not overwrite this function       
        """                                  
        return self.state["input_smooth_adjustment_time_stock_3_of_3"]              
                                             
    def smooth3i_output(self):
        """Type: Flow or Auxiliary
        """
        return self.input_smooth_adjustment_time_flow_3_of_3() 

    def input(self):
        """Type: Flow or Auxiliary
        """
        return self.functions.step(5 , 5) 

    def final_time(self):
        """Type: Flow or Auxiliary
        """
        return 20 

    def initial_time(self):
        """Type: Flow or Auxiliary
        """
        return 0 

    def saveper(self):
        """Type: Flow or Auxiliary
        """
        return self.time_step() 

    def time_step(self):
        """Type: Flow or Auxiliary
        """
        return 0.25 

