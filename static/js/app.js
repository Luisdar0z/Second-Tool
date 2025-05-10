document.getElementById('convert-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const segundos = document.getElementById('inputSegundos').value;

  const response = await fetch('/convert', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ segundos })
  });

  const data = await response.json();
  const resultDiv = document.getElementById('result');

  if (response.ok) {
    resultDiv.textContent = `Tiempo: ${data.resultado}`;
    resultDiv.classList.remove('text-danger');
  } else {
    resultDiv.textContent = data.error || 'Error';
    resultDiv.classList.add('text-danger');
  }
});

// HH:MM:SS a segundos
document.getElementById('to-seconds-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const tiempo = document.getElementById('inputTiempo').value;
  const response = await fetch('/to_seconds', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ tiempo })
  });
  const data = await response.json();
  const resultDiv = document.getElementById('resultToSeconds');
  if (response.ok) {
    resultDiv.textContent = `Segundos: ${data.segundos}`;
    resultDiv.classList.remove('text-danger');
  } else {
    resultDiv.textContent = data.error || 'Error';
    resultDiv.classList.add('text-danger');
  }
});

// Generar múltiples valores aleatorios
document.getElementById('randoms-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const segundos = document.getElementById('inputSegundosRandom').value;
  const cantidad = document.getElementById('inputCantidad').value;
  const response = await fetch('/randoms', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ segundos, cantidad })
  });
  const data = await response.json();
  const resultDiv = document.getElementById('resultRandoms');
  if (response.ok) {
    resultDiv.textContent = `Valores: ${data.valores.join(', ')}`;
    resultDiv.classList.remove('text-danger');
  } else {
    resultDiv.textContent = data.error || 'Error';
    resultDiv.classList.add('text-danger');
  }
});
