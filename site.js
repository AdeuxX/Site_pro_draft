function afficher_all_champ(){
    var liste_all_champ =['aatrox', 'ahri', 'akali', 'akshan', 'alistar', 'amumu', 'anivia', 'annie', 'aphelios', 'ashe', 'aurelion sol', 'azir', 'bard', 'belveth', 'blitzcrank', 'brand', 'braum', 'caitlyn', 'camille', 'cassiopeia', 'chogath', 'corki', 'darius', 'diana', 'dr. mundo', 'draven', 'ekko', 'elise', 'evelynn', 'ezreal', 'fiddlesticks', 'fiora', 'fizz', 'galio', 'gangplank', 'garen', 'gnar', 'gragas', 'graves', 'gwen', 'hecarim', 'heimerdinger', 'illaoi', 'irelia', 'ivern', 'janna', 'jarvan iv', 'jax', 'jayce', 'jhin', 'jinx', 'ksante', 'kaisa', 'kalista', 'karma', 'karthus', 'kassadin', 'katarina', 'kayle', 'kayn', 'kennen', "kha'zix", 'kindred', 'kled', "kog'maw", 'leblanc', 'lee sin', 'leona', 'lillia', 'lissandra', 'lucian', 'lulu', 'lux', 'master yi', 'malphite', 'malzahar', 'maokai', 'milio', 'miss fortune', 'mordekaiser', 'morgana', 'nami', 'nasus', 'nautilus', 'neeko', 'nidalee', 'nilah', 'nocturne', 'nunu', 'olaf', 'orianna', 'ornn', 'pantheon', 'poppy', 'pyke', 'qiyana', 'quinn', 'rakan', 'rammus', 'reksai', 'rell', 'renata glasc', 'renekton', 'rengar', 'riven', 'rumble', 'ryze', 'samira', 'sejuani', 'senna', 'seraphine', 'sett', 'shaco', 'shen', 'shyvana', 'singed', 'sion', 'sivir', 'skarner', 'sona', 'soraka', 'swain', 'sylas', 'syndra', 'tahm-kench', 'taliyah', 'talon', 'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twisted fate', 'twitch', 'udyr', 'urgot', 'varus', 'vayne', 'veigar', 'velkoz', 'vex', 'vi', 'viego', 'viktor', 'vladimir', 'volibear', 'warwick', 'wukong', 'xayah', 'xerath', 'xin zhao', 'yasuo', 'yone', 'yorick', 'yuumi', 'zac', 'zed', 'zeri', 'ziggs', 'zilean', 'zoe', 'zyra']
    var champ_afficher = $("#champ_a_pick").html("");
    liste_all_champ.forEach(function(champ_name){
            var new_img = `<img id="${champ_name}" src='question-mark-png-5a3a530b302187.6463118015137717871972.jpg'>`
            champ_afficher.append(new_img)
            console.log(new_img)

    })
    console.log("salute")
    }

