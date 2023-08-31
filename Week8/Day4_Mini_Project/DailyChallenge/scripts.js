async function getConversionRate(fromCurrency, toCurrency) {
    const apiKey = "3ed12718e28a1ed15bc9b517";
    const url = `https://v6.exchangerate-api.com/v6/${apiKey}/pair/${fromCurrency}/${toCurrency}`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        return data['conversion_rate'];
    } catch (error) {
        console.error("Can not find data", error);
        return null;
    }
}

async function convertCurrency() {
    const fromCurrency = document.getElementById("fromCurrency").value.toUpperCase();
    const toCurrency = document.getElementById("toCurrency").value.toUpperCase();
    const amount = parseFloat(document.getElementById("amount").value);

    try {
        const conversionRate = await getConversionRate(fromCurrency, toCurrency);

        if (conversionRate !== null) {
            const resultElement = document.getElementById("result");
            const convertedAmount = (amount * conversionRate).toFixed(2);
            resultElement.textContent = `${amount} ${fromCurrency} is equal to ${convertedAmount} ${toCurrency}`;
        }
    } catch (error) {
        console.error("Can not convert", error);
    }
}