<template>
  <div>
    <div class="big_screen">
    <div class="input_area">
      <label>age_quantile</label>
      <div class="sub_area">
        <input v-model="age_quantile" type="text" placeholder="Please enter">
      </div>
      <label>hemoglobin</label>
      <div class="sub_area">
        <input v-model="hemoglobin" placeholder="Please enter" >
      </div>
      <label>platelets</label>
      <div class="sub_area">
        <input v-model="platelets" placeholder="Please enter" >
      </div>
      <label>MPV</label>
      <div class="sub_area">
        <input v-model="MPV" placeholder="Please enter" >
      </div>
      <label>RBC</label>
      <div class="sub_area">
        <input v-model="RBC" placeholder="Please enter" >
      </div>
      <label>lymphocytes</label>
      <div class="sub_area">
        <input v-model="lymphocytes" placeholder="Please enter" >
      </div>
      <label>MCHC</label>
      <div class="sub_area">
        <input v-model="MCHC" placeholder="Please enter" >
      </div>
      <label>leukocytes</label>
      <div class="sub_area">
        <input v-model="leukocytes" placeholder="Please enter" >
      </div>
      <label>basophils</label>
      <div class="sub_area">
        <input v-model="basophils" placeholder="Please enter" >
      </div>
      <label>MCH</label>
      <div class="sub_area">
        <input v-model="MCH" placeholder="Please enter" >
      </div>
      <label>eosinophils</label>
      <div class="sub_area">
        <input v-model="eosinophils" placeholder="Please enter" >
      </div>
      <label>MCV</label>
      <div class="sub_area">
        <input v-model="MCV" placeholder="Please enter" >
      </div>
      <label>monocytes</label>
      <div class="sub_area">
        <input v-model="monocytes" placeholder="Please enter" >
      </div>
      <label>RDW</label>
      <div class="sub_area">
        <input v-model="RDW" placeholder="Please enter" >
      </div>
      <label>detection_coronaviridae</label>
      <div class="sub_area">
        <input v-model="detection_coronaviridae" placeholder="Please enter" >
      </div>
      <label>detection_orthomyxoviridae</label>
      <div class="sub_area">
        <input v-model="detection_orthomyxoviridae" placeholder="Please enter" >
      </div>
      <label>detection_paramyxoviridae</label>
      <div class="sub_area">
        <input v-model="detection_paramyxoviridae" placeholder="Please enter" >
      </div>
      <label>detection_picornaviridae</label>
      <div class="sub_area">
        <input v-model="detection_picornaviridae" placeholder="Please enter" >
      </div>
      <label>detection_pneumoviridae</label>
      <div class="sub_area">
        <input v-model="detection_pneumoviridae" placeholder="Please enter" >
      </div>
      <a href="javascript:;" class="button1" @click="onsubmit();">Submit</a>
      </div>
      <div class="drag_upload">
        <input type="file" accept=".csv" id = "fileInputCSV" @change="handleChange()"/>
      </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios';
import detectEthereumProvider from '@metamask/detect-provider';
import Papa from 'papaparse';

export default {
  name: 'Patient',
  data() {
    return {
      age_quantile: '',
      hemoglobin: '',
      platelets: '',
      MPV: '',
      RBC: '',
      lymphocytes: '',
      MCHC: '',
      leukocytes: '',
      basophils: '',
      MCH: '',
      eosinophils: '',
      MCV: '',
      monocytes: '',
      RDW: '',
      detection_coronaviridae: '',
      detection_orthomyxoviridae: '',
      detection_paramyxoviridae: '',
      detection_picornaviridae: '',
      detection_pneumoviridae: '',
    };
  },
  methods: {
    predict(val) {
      const path = 'http://localhost:5000/patient';
      axios.post(path, val)
        .then((response) => {
          console.log('Submit Success.');
          const message = `Our AI predicts your result is ${response.data.answer}.`;
          alert(message);
          console.log(response.data.answer);
        });
    },
    handleChange() {
      const fileInput = document.getElementById('fileInputCSV');
      this.importfxx(fileInput);
    },
    importfxx(obj) {
      console.log(obj);
      let dp;
      Papa.parse(obj.files[0], {
        header: true,
        complete(results) {
          console.log(results);
          dp = results.data;
        },
      });
      setTimeout(() => {
        this.backInput(dp);
      }, 1500);
    },
    backInput(dp) {
      console.log(dp);
      this.age_quantile = dp[0].age_quantile;
      this.hemoglobin = dp[0].hemoglobin;
      this.platelets = dp[0].platelets;
      this.MPV = dp[0].MPV;
      this.RBC = dp[0].RBC;
      this.lymphocytes = dp[0].lymphocytes;
      this.MCHC = dp[0].MCHC;
      this.leukocytes = dp[0].leukocytes;
      this.basophils = dp[0].basophils;
      this.MCH = dp[0].MCH;
      this.eosinophils = dp[0].eosinophils;
      this.MCV = dp[0].MCV;
      this.monocytes = dp[0].monocytes;
      this.RDW = dp[0].RDW;
      this.detection_coronaviridae = dp[0].detection_coronaviridae;
      this.detection_orthomyxoviridae = dp[0].detection_orthomyxoviridae;
      this.detection_paramyxoviridae = dp[0].detection_paramyxoviridae;
      this.detection_picornaviridae = dp[0].detection_picornaviridae;
      this.detection_pneumoviridae = dp[0].detection_pneumoviridae;
    },
    onsubmit() {
      const data = {
        age_quantile: this.age_quantile,
        hemoglobin: this.hemoglobin,
        platelets: this.platelets,
        MPV: this.MPV,
        RBC: this.RBC,
        lymphocytes: this.lymphocytes,
        MCHC: this.MCHC,
        leukocytes: this.leukocytes,
        basophils: this.basophils,
        MCH: this.MCH,
        eosinophils: this.eosinophils,
        MCV: this.MCV,
        monocytes: this.monocytes,
        RDW: this.RDW,
        detection_coronaviridae: this.detection_coronaviridae,
        detection_orthomyxoviridae: this.detection_orthomyxoviridae,
        detection_paramyxoviridae: this.detection_paramyxoviridae,
        detection_picornaviridae: this.detection_picornaviridae,
        detection_pneumoviridae: this.detection_pneumoviridae,
      };
      this.predict(data);
    },
  },
  async mounted() {
    const provider = await detectEthereumProvider();
    if (provider === window.ethereum) {
      window.ethereum.enable().then(() => {
      });
    } else {
      console.log(provider);
      alert('Please use MetaMask');
    }
  },
};
</script>

<style scoped>

.input_area {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.sub_area {
  margin-bottom: 0.5em;
}
.big_screen {
  display: flex;
  justify-content: center;
}
.drag_upload {
  display:inline-block;
  margin-top: 2em;
  margin-left: 2em;
}
</style>
