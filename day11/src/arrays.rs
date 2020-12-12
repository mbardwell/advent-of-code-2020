use std::mem;

pub fn run() {
    let mut numbers: [i32; 5] = [1,2,3,4,5];
    println!("{:?}", numbers);
    numbers[2] = 10;
    println!("{:?} occupies {} bytes", numbers, mem::size_of_val(&numbers));
    let slice: &[i32] = &numbers[0..2];
    println!("{:?}", slice)
}