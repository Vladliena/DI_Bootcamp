import chalk from 'chalk';


function displayColorfulMessage(){
    console.log(chalk.green(
        'I am a green line ' +
        chalk.blue.underline.bold('with a blue substring') +
        ' that becomes green again!'
    ));
}

export default displayColorfulMessage