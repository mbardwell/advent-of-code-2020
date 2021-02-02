open Arg

let verbose = ref false
let filename = ref ""

let main = begin
  let speclist = [
    ("-v", Set verbose, "Useless use file arg");
    ("-n", Set_string filename, "Input file");
  ] in
  let usage_msg = "Give me your file, human. Options available:" in
  parse speclist print_endline usage_msg;
  end

let () = Lwt_main.run begin
  let%lwt bus = OBus_bus.session () in
  Lwt_io.printlf "My unique connection name is: %s" (OBus_connection.name bus)
end