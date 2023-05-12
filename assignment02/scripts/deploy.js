
async function main() {
    const HelloWorld = await ethers.getContractFactory('HelloWorld');

    const hello_wold = await HelloWorld.deploy("Hello, World!");
    console.log(`Contract was deployed to address: ${hello_wold.address}`);
}

main()
    .then(() => process.exit(0))
    .catch(error => {
        console.error(error);
        process.exit(1);
    });
