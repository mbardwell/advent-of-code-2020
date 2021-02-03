open Lwt_io
open Mylib.Ping_pong.Org_foo_bar

let ping proxy msg =
  OBus_method.call m_Ping proxy msg

let _ = Lwt_main.run begin
  let%lwt bus = OBus_bus.session () in
  let proxy = OBus_proxy.make ~peer:(OBus_peer.make ~connection:bus ~name:"org.plop") ~path:["plip"] in
  let%lwt () = printl "trying to ping the pong service" in
  try%lwt
    let%lwt msg = ping proxy "coucou" in
    printlf "rx: %s" msg
  with
    | OBus_bus.Name_has_no_owner msg ->
        let%lwt () = printl ("You must run pong to try this sample!: " ^ msg) in exit 1
    | exn -> Lwt.fail exn
end