use std::io::{ stdin, stdout, Write };

fn read_int (message: &str) -> i32 {
  let mut number_str = String::new();

  print!("{}", message);
  // Ensure that all intermediately buffered contents reach the standard output.
  stdout().flush().expect("error: unable to flush stdout");

  // Read a line from the standard input.
  stdin().read_line(&mut number_str).expect("error: unable to read user input");
  let number: i32 = number_str.trim().parse().expect("error: unable to parse user input into a number");
  
  // Return the number.
  number
}

fn main() {
  println!("TP2: Comparer deux nombres entiers.\n");

  let n1 = read_int("n1 = ");
  let n2 = read_int("n2 = ");

  print!("\nRésultat : "); // newline

  if n1 > n2 {
    println!("{} > {}", n1, n2);
  }
  else if n1 < n2 {
    println!("{} < {}", n1, n2);
  }
  else {
    println!("{} = {}", n1, n2);
  }
}
