window.addEventListener("load", async e => {
  let container = document.getElementById("pins-container");
  let pins = await getPinsJson();

  Object.entries(pins).forEach(([key, value]) => {
    container.appendChild(createInputField(key, value));
  });

  document.getElementById("save").addEventListener("click", e => {
    e.preventDefault();
    updatePins();
  });
});

const getPinsJson = async () => {
  return fetch("/static/text_by_pin.json").then(response => response.json());
};

const getPinsDOM = () => {
  let pins = {};
  document.querySelectorAll(".pin--input").forEach(element => {
    pins[element.dataset.pin] = element.value;
  });
  return pins;
};

const updatePins = async () => {
  let pins = getPinsDOM();
  return fetch("/updatePins", {
    method: "POST",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(pins)
  }).then(response => response.json());
};

const createInputField = (pinNumber, text) => {
  let pin = document.createElement("div");
  pin.setAttribute("id", `pin-${pinNumber}`);
  pin.setAttribute("class", "pin");

  let title = document.createElement("h4");
  title.setAttribute("class", "pin--title");
  title.innerText = `${pinNumber}:`;

  let input = document.createElement("input");
  input.setAttribute("class", "pin--input");
  input.dataset.pin = pinNumber;
  input.value = text;

  pin.appendChild(title);
  pin.appendChild(input);

  return pin;
};