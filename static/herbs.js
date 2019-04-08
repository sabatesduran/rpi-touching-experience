window.addEventListener("load", async e => {
  let socket = io.connect("http://" + document.domain + ":" + location.port);
  socket.on("connect", function() {
    socket.emit("message", {
      data: "I'm connected!"
    });
  });
});
