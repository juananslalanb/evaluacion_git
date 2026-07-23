import random  
import time  
  
    
    def leer_sensor():  
        """simula la lectura de un sensor i2c en un sistema embebido."""  
        valor= round(random.uniform(15.0, 35.0), 2)  
        return valor  
      
      
    if__name__=="__main__":  
        print("___ sistema de monitoreo de temperatura ___")
        for i in range(5):  
            temp=leer_sensor()  
            print(f"muestra [{i+1{/5]: {temp} °c")  
            time.sleep(1)
            print("muestreo finalizado con exito.")  

