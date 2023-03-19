Chart.defaults.global.legend.display = false;
try{
    document.getElementById("input_data").addEventListener("submit", function(event) {
      event.preventDefault();

      var money = document.getElementById("money").value;
      document.getElementById("money_t").innerH
      var oxygen = document.getElementById("oxygen").value;
      var fuel = document.getElementById("fuel").value;
      event.target.reset();
      console.log("o2: " + O + "  " + "F: " + F);

      fetch('http://localhost:5000/api/session/get-session', {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            "money": money;
            "oxygen": oxygen,
            "fuel": fuel,
          }),
        })
          .then(response => {
            if (!response.ok) {
                alert("Ой, что-то пошло не так");
                console.log('Покупка говна');
            }else{
                alert("Покупка прошла успешно");
                console.log('Покупка прошла');
            }

          })
          .catch(eerror => console.error(error));
    });
}catch{}

async function getApiData() {
  const response = await fetch("http://localhost:5000/api/points/get-points");
  const data = await response.json();
  return data.data[0];
}
//const data = await getApiData();
const data = [20,30,40]
const ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: data,
    lineTension: 0.3,
});
new Grid({
  data: data,
  columns: ['Point', 'SH', 'DISTANCE']
}).render(document.getElementById('wrapper'));

