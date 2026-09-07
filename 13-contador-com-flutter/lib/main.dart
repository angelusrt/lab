import 'package:flutter/material.dart';
import 'package:sqflite_common_ffi/sqflite_ffi.dart' as sqlite;

void main() {
  runApp(const MyApp());
}

class AppDatabase {
  static sqlite.Database? _database;

  static Future<sqlite.Database> getDatabase() async {
    if (_database != null) {
      return _database!;
    }

    _database = await sqlite.databaseFactoryFfi.openDatabase(
      'counter.db',
      options: sqlite.OpenDatabaseOptions(
        version: 1,
        onCreate: (db, version) async {
          await db.execute('''
            CREATE TABLE IF NOT EXISTS config (
              id INTEGER PRIMARY KEY,
              count INTEGER NOT NULL
            )
          ''');

		  List rows = await db.rawQuery(
			  "SELECT * FROM config LIMIT 1;"
		  );

		  if (rows.isEmpty) {
			await db.rawInsert("INSERT INTO config (id, count) VALUES (1, 0)");
		  }
        },
      ),
    );

    return _database!;
  }

  static Future<int> getCount() async {
	final sqlite.Database db = await AppDatabase.getDatabase();

	List <Map<String, Object?>>rows = await db.rawQuery("SELECT count FROM config LIMIT 1;");

	if (rows.isEmpty) {
	  return 0;
	}

	return (rows.first['count'] as int?) ?? 0;
  }

  static Future<void> updateCount(int count) async {
	final sqlite.Database db = await AppDatabase.getDatabase();

	try {
		await db.rawInsert(
			"UPDATE config SET count = ? WHERE id = 1",
			[count]
		);
	} catch (error) {
		print(error.toString());
		rethrow;
	}
  }
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: .fromSeed(seedColor: Colors.deepPurple),
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  final TextEditingController _numberController = TextEditingController();

  int _counter = 0;

  void _incrementCounter() async {
    setState(() {
      _counter++;
    });

	await AppDatabase.updateCount(_counter);
  }

  void _decrementCounter() async {
	  if (_counter > 0) {
		setState(() {
			_counter--;
		});
		
		await AppDatabase.updateCount(_counter);
	  }
  }

  Future<void> loadCounter() async {
    final count = await AppDatabase.getCount();
  
    setState(() {
      _counter = count;
    });
  }

  @override
  void initState() {
    super.initState();
    loadCounter();
  }

  @override
  void dispose() {
    _numberController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: .center,
          children: [
            const Text('You have pushed the button this many times:'),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
            Row(
              mainAxisAlignment: .center,
              children: [
                TextButton(
                  onPressed: _decrementCounter,
                  child: const Icon(Icons.minimize),
                ),
                TextButton(
                  onPressed: _incrementCounter,
                  child: const Icon(Icons.add),
                ),
              ],
            ),
            const Text("This is another thing:"),
            Form(
              key: _formKey,
              child: Column(
                children: [
                  TextFormField(
					controller: _numberController,
                    decoration: const InputDecoration(
                      hintText: 'Enter your number',
                    ),
                    validator: (String? value) {
                      if (value != null && int.tryParse(value) == null) {
                        return "Invalid Number";
                      }

                      return null;
                    },
                  ),
                  Padding(
                    padding: const .symmetric(vertical: 16.0),
                    child: ElevatedButton(
                      onPressed: () async {
                        if (_formKey.currentState!.validate()) {
							int number = int.parse(_numberController.text);

							setState(() {
								_counter = number;
							});

							await AppDatabase.updateCount(number);
                        }
                      },
                      child: const Text('Submit'),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
