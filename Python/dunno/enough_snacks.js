
function areSnacksEnough(snacksPerBox, employeesPerFloor) {
    const totalSnacks = snacksPerBox.reduce((sum, val) => sum + val, 0);
    const totalEmployees = employeesPerFloor.reduce((sum, val) => sum + val, 0);
    return totalSnacks >= totalEmployees;
}