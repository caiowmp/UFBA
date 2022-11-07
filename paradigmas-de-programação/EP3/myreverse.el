; Letra g
(defun MYREVERSE (list)
    (setf list-aux nil )
    (loop for x from 1 to (length list) do
          (setf list-aux (cons (first list) list-aux) ) 
          (setf list (rest list))
          )
    (print list-aux)
)

; Testes Letra g
 (MYREVERSE '(1 2 3 4 5 6 7 8 9))