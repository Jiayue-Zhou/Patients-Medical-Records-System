pragma solidity >=0.8.0 < 0.9.0;
//pragma experimental ABIEncoderV2

contract PatientRecord {

    uint256 index = 0;

    struct People {
        uint256 id;
//        uint8 age_quantile;
        uint8 covid19_Res;
        string aggregation;
//        string hemoglobin;
//        string platelets;
//        string MPV;
//        string RBC;
//        string lymphocytes;
//        string MCHC;
//        string leukocytes;
//        string basophils;
//        string MCH;
//        string eosinophils;
//        string MCV;
//        string monocytes;
//        string RDW;
//        string fiveNumber;
//        uint256 detection_coronaviridae;
//        uint256 detection_orthomyxoviridae;
//        uint256 detection_paramyxoviridae;
//        uint256 detection_picornaviridae;
//        uint256 detection_pneumoviridae;
    }
    People[] public people;
    mapping(uint256 => People) public idToPeople;

    function helloWorld() external pure returns(string memory) {
        return "Hello World!";
    }

//    function testStore(uint256 patient_age_quantile, uint256 sars_cov_exam_result, string memory hemoglobin)
//        external {
//
//
//        People memory newPeople = People(index, patient_age_quantile, sars_cov_exam_result, hemoglobin);
//        people.push(newPeople);
//        idToPeople[index] = newPeople;
//        index++;
//
//    }
    function storeData(uint8 covid19_Res, string memory aggregation)
        external {

        People memory newPeople = People(index, covid19_Res, aggregation);

        people.push(newPeople);
        idToPeople[index] = newPeople;
        index++;
    }

//    function storeData(uint8 age_quantile, uint8 covid19_Res, string memory hemoglobin,
//        string memory platelets, string memory MPV, string memory RBC, string memory lymphocytes,
//        string memory MCHC, string memory leukocytes, string memory basophils,
//        string memory MCH, string memory eosinophils, string memory MCV,
//        string memory monocytes, string memory RDW, uint256 detection_coronaviridae, uint256 detection_orthomyxoviridae,
//        uint256 detection_paramyxoviridae, uint256 detection_picornaviridae, uint256 detection_pneumoviridae)
//        external {
//
//
//        People memory newPeople = People(index, age_quantile, covid19_Res,
//            hemoglobin, platelets, MPV, RBC, lymphocytes, MCHC, leukocytes, basophils,  MCH, eosinophils, MCV,
//            monocytes, RDW, detection_coronaviridae, detection_orthomyxoviridae, detection_paramyxoviridae,
//            detection_picornaviridae, detection_pneumoviridae);
//
//        people.push(newPeople);
//        idToPeople[index] = newPeople;
//        index++;
//    }

    function getData(uint256 id) external view returns(string memory) {
        return idToPeople[id].aggregation;
    }

    function getTotal() external view returns(People[] memory) {
        return people;
    }

    function getCovidResult(uint256 id) external view returns(uint8) {
        return idToPeople[id].covid19_Res;
    }
    function getPeopleRecordNum() external view returns(uint256) {
        return index;
    }
}