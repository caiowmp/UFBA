; Letra e
(defun MYBUTLAST (n list-1)
    (setf list-aux (reverse list-1) ) 
    (if (>= n (length list-1) ) (print nil) )
    (if (< n (length list-1) ) (loop for x from 1 to n do
                                  (setf list-aux (rest list-aux) )
                                ) )
    (if (< n (length list-1) ) (print (reverse list-aux) ) )
)

; Testes Letra e
 (MYBUTLAST 8 '(1 2 3 4 5 6 7 8) )
 (MYBUTLAST 1 '(1 2 3 4 5 6 7 8) )
 (MYBUTLAST 3 '(1 2 3 4 5 6 7 8) )