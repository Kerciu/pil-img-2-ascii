# Image to ASCII Art Converter

## Description

A simple project covering the problem of transforming an image file into ASCII art.

## Author

Kacper Górski

## Running

To run the program, follow these steps:

1. Make sure you have Python interpreter installed on your computer.
2. Clone this project to your local machine.
3. Open a terminal or command prompt and navigate to the directory containing this project.
4. Execute the following command:

    ```bash
    py ./mainApp.py --file-name <image_file_name> --output-file <output_file_name> [--dim-width <image_width>] [--dim-height <image_height>] [--erase-white]
    ```

    Where:
    - `<image_file_name>`: The path to the image file you want to convert to ASCII art.
    - `<output_file_name>`: The name of the file where the generated ASCII art will be saved.
    - `<image_width>` (optional): The optional width of the resulting image (in pixels). If not specified, the image will be scaled proportionally to the height.
    - `<image_height>` (optional): The optional height of the resulting image (in pixels). If not specified, the image will be scaled proportionally to the width.
    - `--erase-white` (optional): An option to remove white background from the generated ASCII art.

Example:

```bash
py ./mainApp.py --file-name image.jpg --output-file result.txt --dim-width 100 --dim-height 50 --erase-white
```

## Notes

- The `--dim-width` and `--dim-height` arguments are optional. If not provided, the image will be scaled proportionally.
- The `--erase-white` option removes white background from the generated ASCII art.
- Make sure to provide the correct path to the image file and the name of the output file.

---

If you have any questions or suggestions, feel free to ask.

---

                                                                           
                                                                           
                                                                           
                                   |11[|                                   
                            )}}}}}}}}}}[}}}}}\I                            
                         }}}}[]?---?????---?[}}}}{                         
                      {}}}??????----------??????[}}\|                      
                    \}}]?]??------_______------????}}\/                    
                  {\}]]]?----_________________---??]][}{                   
                |\}][]?---______________________---??]]}\{                 
               \\[[]?---__________+++++++__________--?][]}\                
              {}[[]?--_______++++++++++++++++_______---?[[}\{              
             {}[[?---______+++++++++++++++++++++______--?][[\\             
            {}}[?--______+++++++~~~~~~~~~~++++++++_____--?][[\{            
           {}}[?--_____++++++~~~~~~~~~~~~~~~~~++++++_____-?][[\\           
          {}}[?--_____+++++~~~~<<<<<<<<<<<<~~~~~+++++_____-?][[\1          
         {\}[?--____+++++~~~<<<<<<<<<<<<<<<<<<~~~~++++_____-?]}[{I         
        {{}[]--____++++~~~~<<<<<<<<>>>>><<<<<<<<~~~++++_____-?]}}{         
        {[}]?-____++++~~~<<<<<<>>>>>>>>>>>>><<<<<<~~~+++____--?[}{1        
       \\}[?-____++++~~<<<<<>>>>>>>>>i>>>>>>>><<<<<~~~+++____--][[\|       
      |{}[?--___++++~~<<<<<>>>>iiiiiiiiiiii>>>>><<<<~~~+++____-?]}\)       
      {}}]?-____+++~~<<<<>>>>iiiiiiiiiiiiiiii>>>><<<<~~~+++___--?[[1x      
     {{}[?-____+++~~<<<<>>>iiiiiiiiiiiiiiiiiiii>>>><<<~~++++___-?]}\(      
     {\}]?-___+++~~~<<<>>>iiiiiiiiiiiiiiiiiiiiii>>><<<<~~+++____-?[})O     
     {[[?-____+++~~<<<>>i!!iiiiiiiiiiiiiiiiiiiii!!i><<<<~~+++___-?]}\|     
    \{}[?-___+++~~<<<>ii_}\-i!iiiiiiiiiiiiiii!!+}\?>i<<<~~+++____-?[}|     
    \}}]--___+++~~<<>i\UdhhdC\!iiiiiiiiiiiii!]XphhbQ(i><<~~+++___-?[}(Y    
    {[[?-___+++~~<<<itkahhhhahriiiiiiiiiiii!(dohhhhaac<<<~~+++___--]})|    
   I{[[?-___+++~~<<i\ahhhhhhhhaf!iiiiiiiii!\kahhhhhhhou><<~~++____-?[{|    
   {{}]--___+++~<<>-pahhhhhhhhhb]!iiiiiiii<Zahhhhhhhhhh\><~~+++___-?[\|    
   {\}]-____++~~<<irohhhhaahhhhov!iiiiiii!|ahhhhaaahhhaJ><<~+++___-?[}|    
   {[[?-___+++~~<<>0ahhap/(wahham>iiiiiii!Uahhhbj)Oahhhp_<<~~++___--]}|)   
   {[[?-___+++~~<<<Oahad}!!?wahaZ>iiiiiii!Johak1!!+Oohap_<<~~++____-]}(|   
   {[[?-___+++~<<<i(dap\!ii![wab(!iiiiiii!{pad|!ii!-Oakji<<~~+++___-]}(|   
   {[[?-___++~~<<<>i-\_!iiii!+{-!iiiiiiiii!_\-!iiii!<{]i><<~~+++___-?}(|   
   {[]?-___++~~<<<>>i!iiiiiiii!iiiiiiiiiiiii!iiiiiiii!i>><<~~+++___-?})|   
   {[]?-___++~~<<<>>iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii>><<~~+++___-?})|   
   {[]?-___++~~<<<>>iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii>><<~~+++___-?})|   
   {[]?-___++~~<<<>>iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii>><<~~+++___-?}(|   
   {[[?-___++~~<<<iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii><<~~+++___-?}|(   
   {[[?-___+++~-{1\-<iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii<_}1\?<~+++___-?\|(   
   {[[?-___++~?|1[1||1}-~>iiiiiiiiiiiiiiiiiiiiii>~_[\(|)}{|[~++___--]{|/   
   {}[?-___+++1\` ':<[1||)\\[?_+~<<<<<><<~+_-[}\)||)}+I` '-|_++___--]\|r   
   \\}]-____++(!      ',!}())(||||(())((|||||))(\i:`       (?~+___-?[1|    
   {{}]--___++)I         <\~` :I!><_11_<>il;,`<\+         :(-++___-?})|    
    {[[?-___+~{[:        <\~       ^}[`       >\+       `i}1++___--?{((    
    {[[?-____+?\}+:.     <\~        }[^       >\+     ^i]}{[~+___--]1|(    
    {\}]--___++[}\}-l^   <\~        }[^       >\+  ':<[\\]?_++___-?})|     
    {{}[?-___++~l-}\\[+l ~\~        }[^       >\_:<?}\\[>^!++___--?\)|     
     {[}]--___++;.:~[\\\[[}-; `'.   }[^  .'^,l-}}}\\}-!` ^+++___-?[)|(     
     {\}[?-____++   ^I+]}}}}}}[?-_+_}}++_?][}\}}}[-i,.  .>++___--?{)|      
      {[[?--___++<`    ',_}[]}}\\\\\}}\\\\\}[?]}-^.     l++____-?[)((      
      {\}[?-____++>'     <\~` :I!i>+}[~>i!I,^'>\+      ;+++___--?\)(       
       {[}]--____++>'    <\~        }[`       >\+     :+++____-?}(((       
       \\}[?--___+++<^   <\~       ,}[^       >\+   .I+++____--]))(        
        1}}]?-____+++~:. <\~       ,}[^       >\+  `i+++____--?\(((        
        u1[}]?-____++++i^<\~       ,}[^       >\+.:<+++____--?{((|         
         \\[[]--_____+++~+[~       ,}[^       >}+>++++____--?\()|          
          |\}[]--_____+++++~;^.     }[^     ' >++++++____--?\()|           
           |\}[]--_____+++++++>!;, :[],^ :Ii<++++++_____--?{()|}           
            |1}[]?--_____++++++++++~~~~++++++++++______--?\()(|            
             \)}[]?--______++++++++++++++++++++_______--[)(((I             
              /({[]?---_______++++++++++++++________--?{()(|               
               ||)\[]?--__________________________--?})()(|                
                 \()\[?----_____________________--?})()((Y                 
                   |(){}]?----________________--[{)()((|                   
                    |(((1{}]?----_________--?[{)()(((|                     
                       ((|()1\{\}[[]]][[}{\1)()((((|                       
                         I((||||())))))))((||((((                          
                             }((((||||||((()|                              
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
