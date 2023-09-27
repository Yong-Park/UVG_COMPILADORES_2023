class Fibonacci {

    fibonacci(n: Int) : Int {
        {(
            let f: Int in
            if n = 1 then
                f <- 1
            else
                if n = 2 then
                    f <- 1
                else
                    f <- fibonacci(n-1) + fibonacci(n-2)
                fi
            fi
        );}
    };

};

class Fibonacci2 inherits Fibonacci {
	fiboCall() : Int {
		{
			fibonacci(5);
			self;
		}
	};

};

class Main inherits IO {
    n: Int <- 5;
    s: Bool;
    t: Bool;
    myfibonacci: Fibonacci;

    main() : SELF_TYPE {
        {
            n <- 5 + 6;
            s <- (true);
            t <- not s;
            myfibonacci <- new Fibonacci;
            out_int(myfibonacci.fibonacci(n));
        }
    };
};


