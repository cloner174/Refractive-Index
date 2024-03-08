# Refractive-Index



## Usage 

$       git clone https://github.com/cloner174/Refractive-Index.git

$       cd Refractive-Index

$       python3 -m pip install requirements.txt

$       python3 index.py




## How to Do same as that!

To integrate the `Light` class and perform calculations, follow these steps:


1. Create a new file, e.g., `index.py`, in the directory, and immediately add the following line as the first line of the code:


>                  import main

  Or, Like I was done it:

*
>                  from main import Light
*


Now, You have access to Light class that can simply be call and modify by some line like this:


>   Refelected_Values_RandT = Light( landa0 = < some number for start > , 
>                                     landa = < any other number to use for calculation R and T based on! > )


Finally, as the moment you create the object of the class, can see the result by some command like:



>   R_landa , T_landa = ourWork.run()
>
>   print(R_landa)
>   print(T_landa)


''' < You will see your Landa INPUT Number>-NOTlanda0-but-other-one-! 
             < someFloatNumber from the calculation of R >  ''' 

''' same for T !! '''



* In this work, R_landa is represent for R(λ) and T_landa is for T(λ)




## Mistakes and Corrections

To err is human, and nobody likes a perfect person! If you come across any mistakes or if you have questions, feel free to raise an issue or submit a pull request.



* be good! :) and have a lovely experience!
