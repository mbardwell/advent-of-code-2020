mod print;
mod vars;
mod strings;
mod arrays;
mod vectors;

fn main() {
    println!("Hello, World!");
    print::run();
    vars::run();
    strings::run();
    arrays::run();
    vectors::run();
}
