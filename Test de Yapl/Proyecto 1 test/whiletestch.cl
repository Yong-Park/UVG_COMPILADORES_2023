.data
    count:  .word 10
    limit:  .word 5

.text
main:
    la $t0, count          # Cargamos la dirección de count en $t0
    la $t1, limit          # Cargamos la dirección de limit en $t1

while_loop:
    lw $t2, 0($t0)         # Cargamos el valor de count en $t2
    lw $t3, 0($t1)         # Cargamos el valor de limit en $t3

    beq $t2, $t3, end_loop # Si count == limit, salimos del bucle
    # Si la condición no se cumple, continuamos con el bucle

    # Coloca aquí el código que deseas ejecutar en el bucle.

    # Al final del bucle, actualiza el contador (count) si es necesario
    addi $t2, $t2, 1      # Incrementa count en 1
    sw $t2, 0($t0)        # Almacena el nuevo valor de count

    j while_loop          # Salta de nuevo al inicio del bucle

end_loop:
    # Coloca aquí el código que deseas ejecutar después del bucle while.

    # Termina el programa
    li $v0, 10
    syscall