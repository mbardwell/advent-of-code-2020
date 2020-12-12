pub fn run() {
    let mut numbers: Vec<i32> = vec![1,2,3,4,5];
    println!("{:?}", numbers);
    numbers[2] = 10;
    numbers.push(5);
    println!("{:?} occupies {} bytes", numbers, numbers.len());
    numbers.pop();
    let slice: &[i32] = &numbers[0..2];
    println!("{:?}", slice);

    for x in numbers.iter() {
        println!("Vector numbers: {}", x)
    }

    for x in numbers.iter_mut() {
        *x *= 2;
    }
    println!("Vector numbers: {:?}", numbers)
}