pub fn run() {
    let name = "Mike";
    let mut age = 26;
    println!("{} is {}", name, age);
    age = 27;
    println!("{} is {}", name, age);

    let (x,y) = (2,3);
    println!("x: {} y: {}", x, y);

    let set_type: bool = true;
    println!("{}", set_type);

    let face = '\u{1F600}';
    println!("{}", face);
}