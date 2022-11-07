; Letra c
(defun MYLENGTH (list-1)
    (setq tamanho 0)
    (dolist (item list-1)
        (setf tamanho (+ tamanho 1))
    )
    (print tamanho)
)

; Testes Letra c
 (MYLENGTH '(1 2 3 4 5 6 7 8 9) )
 (MYLENGTH '(1 2 3 4 5 6 9) )