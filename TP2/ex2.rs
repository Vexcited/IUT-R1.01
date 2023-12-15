use std::io::{ stdin, stdout, Write };

fn read_int (message: &str) -> i32 {
  let mut number_str = String::new();

  print!("{}", message);
  // Ensure that all intermediately buffered contents reach the standard output.
  stdout().flush().unwrap();

  // Read a line from the standard input.
  stdin().read_line(&mut number_str).unwrap();
  let number: i32 = number_str.trim().parse().expect("Veuillez entrer un nombre entier.");
  
  // Return the number.
  number
}

fn main() {
  println!("TP2.Ex2: Compare two integers.\n");

  let n1 = read_int("n1 = ");
  let n2 = read_int("n2 = ");

  print!("\nResult : ");

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
