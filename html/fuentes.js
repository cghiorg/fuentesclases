function validarFormulario() {
    let nombre = document.getElementById('nombre').value;
    if (nombre.trim() === '') {
      alert('Por favor, ingresá tu nombre.');
      return false;
    }
  }