// https://www.youtube.com/watch?v=zF34dRivLOw  at 34 min
// Primitive str: immutable
// String = growablem heap-allocated data structure

pub fn run() {
    let _hello = String::from("Hello"); // String
    let _a = "hi"; // primitive

    let mut hello_mut = String::from("Hello, "); // String
    hello_mut.push('W');
    hello_mut.push_str("orld!");
    println!("{} size {}", hello_mut, hello_mut.capacity());
}