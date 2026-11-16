// Named Export
export const formatPrice = (value) =>{
    return new Intl.NumberFormat('th-TH', { style: 'currency', currency: 'THB' }).format(value);
}
// console.log(formatPrice(2490));

export const vat_rate = 0.07;

export const calculateVat = (value) => {
    return value * vat_rate;
}

export default function calculateVat2(value) {
    return value * vat_rate;
};