//Yo practicando JavaScript, porque photoshop se programa con JavaScript y mi novia trabaja en algo que se puede automatizar muy fácilmente. Así que ahora aprendo un toque de JavaScript también.
//Función que toma ordenes de pizza

var orderCount = 0; //crea variable "orderCount" y la settea a cero

function takeOrder(topping, crustType) {
  console.log('Order: ' + crustType + ' crust topped with ' + topping);
  orderCount = orderCount + 1;
}

//cada vez que se llama a esta función, le suma +1 a order count

function getSubTotal(itemCount) {
  return itemCount * 7.5;
}

takeOrder('bacon', 'thin');
takeOrder('pepperoni', 'regular');
takeOrder('pesto', 'thin');

console.log(getSubTotal(orderCount));